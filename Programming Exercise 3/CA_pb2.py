# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CA.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08\x43\x41.proto\"9\n\nClientInfo\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x18\n\npublic_key\x18\x02 \x01(\x0b\x32\x04.Key\"\x1b\n\x03Key\x12\t\n\x01\x65\x18\x01 \x01(\t\x12\t\n\x01n\x18\x02 \x01(\t\"8\n\x14RegistrationResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x16\n\x08\x43lientID\x12\n\n\x02id\x18\x01 \x01(\t\"\"\n\x0b\x43\x65rtificate\x12\x13\n\x0b\x63\x65rtificate\x18\x02 \x01(\t2}\n\x14\x43\x65rtificateAuthority\x12\x36\n\x0eRegisterClient\x12\x0b.ClientInfo\x1a\x15.RegistrationResponse\"\x00\x12-\n\x10IssueCertificate\x12\t.ClientID\x1a\x0c.Certificate\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CA_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CLIENTINFO']._serialized_start=12
  _globals['_CLIENTINFO']._serialized_end=69
  _globals['_KEY']._serialized_start=71
  _globals['_KEY']._serialized_end=98
  _globals['_REGISTRATIONRESPONSE']._serialized_start=100
  _globals['_REGISTRATIONRESPONSE']._serialized_end=156
  _globals['_CLIENTID']._serialized_start=158
  _globals['_CLIENTID']._serialized_end=180
  _globals['_CERTIFICATE']._serialized_start=182
  _globals['_CERTIFICATE']._serialized_end=216
  _globals['_CERTIFICATEAUTHORITY']._serialized_start=218
  _globals['_CERTIFICATEAUTHORITY']._serialized_end=343
# @@protoc_insertion_point(module_scope)
