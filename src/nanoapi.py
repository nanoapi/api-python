# Python client to the Nano Node API
# Tested with Python 2.7.13 and Python 3.6.5
# Dependencies: Protobuf (Python 2 also needs 'future')
import core_pb2 as Model
import socket
import sys
import struct
import time
import google.protobuf.descriptor_pb2
from google.protobuf.json_format import MessageToJson, Parse
from builtins import bytes
from future.standard_library import install_aliases
install_aliases()
from urllib.parse import urlparse

class Client:
    """Nano API client"""
    def __init__(self, conn):
        """Initialize client with an IPC connection. The connection object must provide send_query method"""
        self.conn = conn

    def query(self, query_object):
        """Execute query"""
        # Strip off the 'query_' prefix
        undecorated = type(query_object).__name__[6:]

        # Get enum value and send query
        query_id = getattr(Model, undecorated.upper())
        res = self.conn.send_query(query_id, query_object)

        # Create result object
        res_obj = getattr(Model, 'res_' + undecorated.lower())()
        res_obj.ParseFromString(res)
        return res_obj

    def to_json(self, obj):
        """Convert the protobuf object to JSON"""
        return MessageToJson(obj, preserving_proto_field_name=True, indent=4)

    def from_json(self, query_name, json):
        """Create a query_<query_name> protobuf object and parse the supplied JSON into it"""
        query_obj = getattr(Model, 'query_' + query_name.lower())()
        return Parse(json, query_obj)

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
            sys.exit(1)

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

    def send_query(self, query_type, query):
        """Serialize query and send via socket, deserialize and return result"""
        header = Model.query()
        header.type = query_type
        str_header = header.SerializeToString()
        str_query = query.SerializeToString()

        # <i is little endian 32-bit
        packed_heading = struct.pack(">i%ds" % (len(str_header),), len(str_header), str_header)
        packed_query = struct.pack(">i%ds" % (len(str_query),), len(str_query), str_query)
        self.sock.sendall(packed_heading)
        self.sock.sendall(packed_query)

        # Get response
        response_buf = self.recvall(self.sock, 4)
        header_len = struct.unpack('>i', response_buf[:4])[0]
        #print >> sys.stderr, "Got response header length: %d " % header_len

        response_buf = self.recvall(self.sock, header_len)

        response = Model.response();
        response.ParseFromString(response_buf);
        #print >> sys.stderr, "Got response type: %d " % response.type

        # Length of response
        response_buf = bytes('','utf-8')
        while len(response_buf) < 4:
            response_buf += self.sock.recv(1)
        header_len = struct.unpack('>i', response_buf[:4])[0]

        # Response
        response_buf = bytes('','utf-8')
        while len(response_buf) < header_len:
            response_buf += self.sock.recv(1)
        return response_buf
