# Python client for the Nano Node API
# Tested with Python 2.7.13 and Python 3.6.5
import glob
import os
import core_pb2 as Core
import socket
import sys
import struct
import time
from google.protobuf.message import Message
import google.protobuf.descriptor_pb2
from google.protobuf.json_format import MessageToJson, Parse
from builtins import bytes
from future.standard_library import install_aliases
install_aliases()
from urllib.parse import urlparse
from threading import Lock

proto_modules = [Core]

# Dynamically import all proto-generated modules
proto_files = glob.glob('**/*_pb2.py')
for proto_file in proto_files:
    basename = os.path.basename(proto_file)
    noext = basename[:-3]

    # Already imported
    if noext != "core_pb2":
        proto_mod = basename[:-7].capitalize()
        imported = __import__(noext)
        proto_modules.append(imported) 

class Session:
    """A node session """
    def __init__(self, conn):
        """Initialize client with an IPC connection. The connection object must provide send_request method"""
        self.conn = conn
        self.lock = Lock()

        # Extract request types
        #self.query_types = [v for v in  vars(Core).values() if isinstance(v, type) and issubclass(v, Message) and v.__name__.startswith("req_")]
        #for clazz in self.query_types:
        #    print (clazz.__name__)
        #    print (clazz.DESCRIPTOR.fields_by_name.keys())
        #    print ([f.type for f in clazz.DESCRIPTOR.fields])

    def getattr_multi(self, objarray, symbol):
        """Returns the attribute 'symbol' in any of the objects in objarray, or None if not found"""
        for obj in objarray:
            attr = getattr(obj, symbol, None)
            if attr is not None:
                return attr
        return None

    def request(self, req_object):
        self.lock.acquire()
        try:
            """Send request"""
            # Strip off the 'req_' prefix
            undecorated = type(req_object).__name__[4:]

            # Get enum value and send req
            req_id = getattr(Core, undecorated.upper())
            error, res = self.conn.send_request(req_id, req_object)
            if error is None:
                # Create result object
                res_obj = self.getattr_multi(proto_modules, 'res_' + undecorated.lower())()
                res_obj.ParseFromString(res)
                return res_obj
            else:
                err_obj = Core.response()
                err_obj.ParseFromString(error)
                return err_obj
        finally:
            self.lock.release()

    def to_json(self, obj):
        """Convert the protobuf object to JSON"""
        return MessageToJson(obj, preserving_proto_field_name=True, indent=4)

    def from_json(self, req_name, json):
        """Create a req_<req_name> protobuf object and parse the supplied JSON into it"""
        msg = self.getattr_multi(proto_modules, 'req_' + req_name.lower())
        if msg != None:
            return Parse(json, msg())
        else:
            return None

    def error_response(self, code, message):
        """Create an error response given an error code and message"""
        err_obj = Core.response()
        err_obj.error_code = code
        err_obj.error_message = message
        err_obj.error_category = "generic"
        return err_obj

    def error_response_from_exception(self, ex):
        """Create an error response given an exception. The error code is set to 1."""
        err_obj = Core.response()
        err_obj.error_code = 1
        err_obj.error_message = str(ex)
        err_obj.error_category = "exception"
        return err_obj

class SocketConnection:
    """TCP or domain socket connection to the IPC server"""
    def __init__(self, address):
        """Initialize socket with a tcp:/// or local:/// connection."""
        self.address = address
        try:
            url = urlparse(self.address)
            if (url.scheme.lower() == "local"):
                self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self.sock.connect(url.path)
            elif (url.scheme.lower() == "tcp"):
                self.sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
                self.sock.connect((url.path, url.port))
            else:
                raise ValueError('Invalid scheme', url.scheme)
        except socket.error as msg:
            print >>sys.stderr, msg

    def close (self):
        """Close socket connection"""
        self.sock.close()

    def recvall(self, sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def send_request(self, request_type, request):
        """Serialize request and send via socket, deserialize and return result"""
        try:
            # Send preamble
            preamble = bytearray([ord('N'),0, Core.VERSION_MAJOR, Core.VERSION_MINOR])
            self.sock.sendall(preamble)

            # Request header
            header = Core.request()
            header.type = request_type
            str_header = header.SerializeToString()
            str_request = request.SerializeToString()

            # <i is little endian 32-bit
            packed_heading = struct.pack(">i%ds" % (len(str_header),), len(str_header), str_header)
            packed_request = struct.pack(">i%ds" % (len(str_request),), len(str_request), str_request)
            self.sock.sendall(packed_heading)
            self.sock.sendall(packed_request)

            # Get preamble
            preamble = self.recvall(self.sock, 4)
            if chr(preamble[0]) != 'N':
                raise ValueError('Invalid preamble')
            if int(preamble[2]) > Core.VERSION_MAJOR:
                raise ValueError('Unsupport API version')

            # Get response header
            response_buf = self.recvall(self.sock, 4)
            header_len = struct.unpack('>i', response_buf[:4])[0]

            response_buf = self.recvall(self.sock, header_len)
            response = Core.response();
            response.ParseFromString(response_buf);

            if response.error_code == 0:
                # Length of response
                response_buf = bytes('','utf-8')
                while len(response_buf) < 4:
                    response_buf += self.sock.recv(1)
                header_len = struct.unpack('>i', response_buf[:4])[0]

                # Response
                response_buf = bytes('','utf-8')
                while len(response_buf) < header_len:
                    response_buf += self.sock.recv(1)
                return None, response_buf
            else:
                return response_buf, None

        except Exception as msg:
            response = Core.response()
            response.error_code = 1
            response.error_message = str(msg)
            return response.SerializeToString(), None
