# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='core.proto',
  package='nano.api',
  syntax='proto3',
  serialized_pb=_b('\n\ncore.proto\x12\x08nano.api\x1a\x1egoogle/protobuf/wrappers.proto\"*\n\x05query\x12!\n\x04type\x18\x01 \x01(\x0e\x32\x13.nano.api.QueryType\"r\n\x08response\x12 \n\x06result\x18\x01 \x01(\x0e\x32\x10.nano.api.Result\x12!\n\x04type\x18\x02 \x01(\x0e\x32\x13.nano.api.QueryType\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x12\n\nerror_code\x18\x04 \x01(\x11\"S\n\x14query_client_connect\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\r\x12\x15\n\rapi_client_id\x18\x02 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x03 \x01(\t\"a\n\x12res_client_connect\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\r\x12\x1a\n\x12node_version_major\x18\x02 \x01(\r\x12\x1a\n\x12node_version_patch\x18\x03 \x01(\r\"\x18\n\nquery_ping\x12\n\n\x02id\x18\x01 \x01(\r\"\x16\n\x08res_ping\x12\n\n\x02id\x18\x01 \x01(\r\"i\n\x15query_account_pending\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x04\x12/\n\tthreshold\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"A\n\x13res_account_pending\x12*\n\x07pending\x18\x01 \x03(\x0b\x32\x19.nano.api.account_pending\"\\\n\x0f\x61\x63\x63ount_pending\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x38\n\nblock_info\x18\x02 \x03(\x0b\x32$.nano.api.account_pending_block_info\"J\n\x1a\x61\x63\x63ount_pending_block_info\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t*{\n\tQueryType\x12\n\n\x06UNKOWN\x10\x00\x12\x15\n\x11REGISTER_CALLBACK\x10\x01\x12\x08\n\x04PING\x10\x02\x12\x13\n\x0f\x41\x43\x43OUNT_BALANCE\x10\x03\x12\x17\n\x13\x41\x43\x43OUNT_BLOCK_COUNT\x10\x04\x12\x13\n\x0f\x41\x43\x43OUNT_PENDING\x10\x05*D\n\x06Result\x12\x06\n\x02OK\x10\x00\x12\x11\n\rGENERIC_ERROR\x10\x01\x12\x11\n\rINVALID_INPUT\x10\x02\x12\x0c\n\x08IO_ERROR\x10\x03\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])

_QUERYTYPE = _descriptor.EnumDescriptor(
  name='QueryType',
  full_name='nano.api.QueryType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_CALLBACK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_BALANCE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_BLOCK_COUNT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_PENDING', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=794,
  serialized_end=917,
)
_sym_db.RegisterEnumDescriptor(_QUERYTYPE)

QueryType = enum_type_wrapper.EnumTypeWrapper(_QUERYTYPE)
_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='nano.api.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERIC_ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_INPUT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IO_ERROR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=919,
  serialized_end=987,
)
_sym_db.RegisterEnumDescriptor(_RESULT)

Result = enum_type_wrapper.EnumTypeWrapper(_RESULT)
UNKOWN = 0
REGISTER_CALLBACK = 1
PING = 2
ACCOUNT_BALANCE = 3
ACCOUNT_BLOCK_COUNT = 4
ACCOUNT_PENDING = 5
OK = 0
GENERIC_ERROR = 1
INVALID_INPUT = 2
IO_ERROR = 3



_QUERY = _descriptor.Descriptor(
  name='query',
  full_name='nano.api.query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='nano.api.query.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=98,
)


_RESPONSE = _descriptor.Descriptor(
  name='response',
  full_name='nano.api.response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='nano.api.response.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='nano.api.response.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='nano.api.response.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='nano.api.response.error_code', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=214,
)


_QUERY_CLIENT_CONNECT = _descriptor.Descriptor(
  name='query_client_connect',
  full_name='nano.api.query_client_connect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_version', full_name='nano.api.query_client_connect.api_version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_client_id', full_name='nano.api.query_client_connect.api_client_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_key', full_name='nano.api.query_client_connect.api_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=299,
)


_RES_CLIENT_CONNECT = _descriptor.Descriptor(
  name='res_client_connect',
  full_name='nano.api.res_client_connect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_version', full_name='nano.api.res_client_connect.api_version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_version_major', full_name='nano.api.res_client_connect.node_version_major', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_version_patch', full_name='nano.api.res_client_connect.node_version_patch', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=398,
)


_QUERY_PING = _descriptor.Descriptor(
  name='query_ping',
  full_name='nano.api.query_ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='nano.api.query_ping.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=400,
  serialized_end=424,
)


_RES_PING = _descriptor.Descriptor(
  name='res_ping',
  full_name='nano.api.res_ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='nano.api.res_ping.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=448,
)


_QUERY_ACCOUNT_PENDING = _descriptor.Descriptor(
  name='query_account_pending',
  full_name='nano.api.query_account_pending',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accounts', full_name='nano.api.query_account_pending.accounts', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='nano.api.query_account_pending.count', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='nano.api.query_account_pending.threshold', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=555,
)


_RES_ACCOUNT_PENDING = _descriptor.Descriptor(
  name='res_account_pending',
  full_name='nano.api.res_account_pending',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pending', full_name='nano.api.res_account_pending.pending', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=557,
  serialized_end=622,
)


_ACCOUNT_PENDING = _descriptor.Descriptor(
  name='account_pending',
  full_name='nano.api.account_pending',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='nano.api.account_pending.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_info', full_name='nano.api.account_pending.block_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=624,
  serialized_end=716,
)


_ACCOUNT_PENDING_BLOCK_INFO = _descriptor.Descriptor(
  name='account_pending_block_info',
  full_name='nano.api.account_pending_block_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='nano.api.account_pending_block_info.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='nano.api.account_pending_block_info.amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='nano.api.account_pending_block_info.source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=792,
)

_QUERY.fields_by_name['type'].enum_type = _QUERYTYPE
_RESPONSE.fields_by_name['result'].enum_type = _RESULT
_RESPONSE.fields_by_name['type'].enum_type = _QUERYTYPE
_QUERY_ACCOUNT_PENDING.fields_by_name['threshold'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_RES_ACCOUNT_PENDING.fields_by_name['pending'].message_type = _ACCOUNT_PENDING
_ACCOUNT_PENDING.fields_by_name['block_info'].message_type = _ACCOUNT_PENDING_BLOCK_INFO
DESCRIPTOR.message_types_by_name['query'] = _QUERY
DESCRIPTOR.message_types_by_name['response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['query_client_connect'] = _QUERY_CLIENT_CONNECT
DESCRIPTOR.message_types_by_name['res_client_connect'] = _RES_CLIENT_CONNECT
DESCRIPTOR.message_types_by_name['query_ping'] = _QUERY_PING
DESCRIPTOR.message_types_by_name['res_ping'] = _RES_PING
DESCRIPTOR.message_types_by_name['query_account_pending'] = _QUERY_ACCOUNT_PENDING
DESCRIPTOR.message_types_by_name['res_account_pending'] = _RES_ACCOUNT_PENDING
DESCRIPTOR.message_types_by_name['account_pending'] = _ACCOUNT_PENDING
DESCRIPTOR.message_types_by_name['account_pending_block_info'] = _ACCOUNT_PENDING_BLOCK_INFO
DESCRIPTOR.enum_types_by_name['QueryType'] = _QUERYTYPE
DESCRIPTOR.enum_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

query = _reflection.GeneratedProtocolMessageType('query', (_message.Message,), dict(
  DESCRIPTOR = _QUERY,
  __module__ = 'core_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.query)
  ))
_sym_db.RegisterMessage(query)

response = _reflection.GeneratedProtocolMessageType('response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'core_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.response)
  ))
_sym_db.RegisterMessage(response)

query_client_connect = _reflection.GeneratedProtocolMessageType('query_client_connect', (_message.Message,), dict(
  DESCRIPTOR = _QUERY_CLIENT_CONNECT,
  __module__ = 'core_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.query_client_connect)
  ))
_sym_db.RegisterMessage(query_client_connect)

res_client_connect = _reflection.GeneratedProtocolMessageType('res_client_connect', (_message.Message,), dict(
  DESCRIPTOR = _RES_CLIENT_CONNECT,
  __module__ = 'core_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.res_client_connect)
  ))
_sym_db.RegisterMessage(res_client_connect)

query_ping = _reflection.GeneratedProtocolMessageType('query_ping', (_message.Message,), dict(
  DESCRIPTOR = _QUERY_PING,
  __module__ = 'core_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.query_ping)
  ))
_sym_db.RegisterMessage(query_ping)

res_ping = _reflection.GeneratedProtocolMessageType('res_ping', (_message.Message,), dict(
  DESCRIPTOR = _RES_PING,
  __module__ = 'core_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.res_ping)
  ))
_sym_db.RegisterMessage(res_ping)

query_account_pending = _reflection.GeneratedProtocolMessageType('query_account_pending', (_message.Message,), dict(
  DESCRIPTOR = _QUERY_ACCOUNT_PENDING,
  __module__ = 'core_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.query_account_pending)
  ))
_sym_db.RegisterMessage(query_account_pending)

res_account_pending = _reflection.GeneratedProtocolMessageType('res_account_pending', (_message.Message,), dict(
  DESCRIPTOR = _RES_ACCOUNT_PENDING,
  __module__ = 'core_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.res_account_pending)
  ))
_sym_db.RegisterMessage(res_account_pending)

account_pending = _reflection.GeneratedProtocolMessageType('account_pending', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT_PENDING,
  __module__ = 'core_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.account_pending)
  ))
_sym_db.RegisterMessage(account_pending)

account_pending_block_info = _reflection.GeneratedProtocolMessageType('account_pending_block_info', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT_PENDING_BLOCK_INFO,
  __module__ = 'core_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.account_pending_block_info)
  ))
_sym_db.RegisterMessage(account_pending_block_info)


# @@protoc_insertion_point(module_scope)
