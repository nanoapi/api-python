# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accounts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='accounts.proto',
  package='nano.api',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x61\x63\x63ounts.proto\x12\x08nano.api\x1a\x1egoogle/protobuf/wrappers.proto\"w\n\x13req_account_pending\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x04\x12\x0e\n\x06source\x18\x03 \x01(\x08\x12/\n\tthreshold\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"A\n\x13res_account_pending\x12*\n\x07pending\x18\x01 \x03(\x0b\x32\x19.nano.api.account_pending\"\\\n\x0f\x61\x63\x63ount_pending\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x38\n\nblock_info\x18\x02 \x03(\x0b\x32$.nano.api.account_pending_block_info\"J\n\x1a\x61\x63\x63ount_pending_block_info\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_REQ_ACCOUNT_PENDING = _descriptor.Descriptor(
  name='req_account_pending',
  full_name='nano.api.req_account_pending',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accounts', full_name='nano.api.req_account_pending.accounts', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='nano.api.req_account_pending.count', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='nano.api.req_account_pending.source', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='nano.api.req_account_pending.threshold', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=60,
  serialized_end=179,
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
  serialized_start=181,
  serialized_end=246,
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
  serialized_start=248,
  serialized_end=340,
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
  serialized_start=342,
  serialized_end=416,
)

_REQ_ACCOUNT_PENDING.fields_by_name['threshold'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_RES_ACCOUNT_PENDING.fields_by_name['pending'].message_type = _ACCOUNT_PENDING
_ACCOUNT_PENDING.fields_by_name['block_info'].message_type = _ACCOUNT_PENDING_BLOCK_INFO
DESCRIPTOR.message_types_by_name['req_account_pending'] = _REQ_ACCOUNT_PENDING
DESCRIPTOR.message_types_by_name['res_account_pending'] = _RES_ACCOUNT_PENDING
DESCRIPTOR.message_types_by_name['account_pending'] = _ACCOUNT_PENDING
DESCRIPTOR.message_types_by_name['account_pending_block_info'] = _ACCOUNT_PENDING_BLOCK_INFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

req_account_pending = _reflection.GeneratedProtocolMessageType('req_account_pending', (_message.Message,), dict(
  DESCRIPTOR = _REQ_ACCOUNT_PENDING,
  __module__ = 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.req_account_pending)
  ))
_sym_db.RegisterMessage(req_account_pending)

res_account_pending = _reflection.GeneratedProtocolMessageType('res_account_pending', (_message.Message,), dict(
  DESCRIPTOR = _RES_ACCOUNT_PENDING,
  __module__ = 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.res_account_pending)
  ))
_sym_db.RegisterMessage(res_account_pending)

account_pending = _reflection.GeneratedProtocolMessageType('account_pending', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT_PENDING,
  __module__ = 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.account_pending)
  ))
_sym_db.RegisterMessage(account_pending)

account_pending_block_info = _reflection.GeneratedProtocolMessageType('account_pending_block_info', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT_PENDING_BLOCK_INFO,
  __module__ = 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:nano.api.account_pending_block_info)
  ))
_sym_db.RegisterMessage(account_pending_block_info)


# @@protoc_insertion_point(module_scope)
