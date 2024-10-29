# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: order_management.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'order_management.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16order_management.proto\x12\x10order_management\"\x92\x01\n\x05Order\x12\x14\n\x0cproduct_name\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\t\x12\x17\n\x0fpayment_gateway\x18\x03 \x01(\t\x12\x12\n\ncard_brand\x18\x04 \x01(\t\x12\x0c\n\x04\x62\x61nk\x18\x05 \x01(\t\x12\x1a\n\x12shipping_direction\x18\x06 \x01(\t\x12\r\n\x05\x65mail\x18\x07 \x01(\t\"!\n\rOrderResponse\x12\x10\n\x08order_id\x18\x01 \x01(\t\"&\n\x12OrderStatusRequest\x12\x10\n\x08order_id\x18\x01 \x01(\t\"%\n\x13OrderStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xb9\x01\n\x0fOrderManagement\x12G\n\x0b\x43reateOrder\x12\x17.order_management.Order\x1a\x1f.order_management.OrderResponse\x12]\n\x0eGetOrderStatus\x12$.order_management.OrderStatusRequest\x1a%.order_management.OrderStatusResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'order_management_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ORDER']._serialized_start=45
  _globals['_ORDER']._serialized_end=191
  _globals['_ORDERRESPONSE']._serialized_start=193
  _globals['_ORDERRESPONSE']._serialized_end=226
  _globals['_ORDERSTATUSREQUEST']._serialized_start=228
  _globals['_ORDERSTATUSREQUEST']._serialized_end=266
  _globals['_ORDERSTATUSRESPONSE']._serialized_start=268
  _globals['_ORDERSTATUSRESPONSE']._serialized_end=305
  _globals['_ORDERMANAGEMENT']._serialized_start=308
  _globals['_ORDERMANAGEMENT']._serialized_end=493
# @@protoc_insertion_point(module_scope)
