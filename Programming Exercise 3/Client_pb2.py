# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Client.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x43lient.proto\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"*\n\x0f\x41\x63knowledgement\x12\x17\n\x0f\x61\x63knowledgement\x18\x01 \x01(\t2E\n\x13\x43lientCommunication\x12.\n\x0eReceiveMessage\x12\x08.Message\x1a\x10.Acknowledgement\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Client_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MESSAGE']._serialized_start=16
  _globals['_MESSAGE']._serialized_end=42
  _globals['_ACKNOWLEDGEMENT']._serialized_start=44
  _globals['_ACKNOWLEDGEMENT']._serialized_end=86
  _globals['_CLIENTCOMMUNICATION']._serialized_start=88
  _globals['_CLIENTCOMMUNICATION']._serialized_end=157
# @@protoc_insertion_point(module_scope)
