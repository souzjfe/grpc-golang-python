# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: math.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmath.proto\x12\x08protobuf\"$\n\x07Request\x12\x0b\n\x03num\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"(\n\x08Response\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t2:\n\x04Math\x12\x32\n\x03Max\x12\x11.protobuf.Request\x1a\x12.protobuf.Response\"\x00(\x01\x30\x01\x42\x14Z\x12\x62idirecional/protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'math_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\022bidirecional/proto'
  _globals['_REQUEST']._serialized_start=24
  _globals['_REQUEST']._serialized_end=60
  _globals['_RESPONSE']._serialized_start=62
  _globals['_RESPONSE']._serialized_end=102
  _globals['_MATH']._serialized_start=104
  _globals['_MATH']._serialized_end=162
# @@protoc_insertion_point(module_scope)
