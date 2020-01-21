# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diagnostics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import empty_pb2 as empty__pb2
from . import node_pb2 as node__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='diagnostics.proto',
  package='io.casperlabs.node.api.diagnostics',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x64iagnostics.proto\x12\"io.casperlabs.node.api.diagnostics\x1a\x0b\x65mpty.proto\x1a\nnode.proto\"\xfd\x01\n\x0fNodeCoreMetrics\x12\x19\n\x11pingReceiverCount\x18\x01 \x01(\x03\x12\x1b\n\x13lookupReceiverCount\x18\x02 \x01(\x03\x12\x1f\n\x17\x64isconnectReceiverCount\x18\x03 \x01(\x03\x12\x10\n\x08\x63onnects\x18\x04 \x01(\x03\x12+\n#p2pEncryptionHandshakeReceiverCount\x18\x05 \x01(\x03\x12)\n!p2pProtocolHandshakeReceiverCount\x18\x06 \x01(\x03\x12\r\n\x05peers\x18\x07 \x01(\x03\x12\x0c\n\x04\x66rom\x18\x08 \x01(\x03\x12\n\n\x02to\x18\t \x01(\x03\":\n\x05Peers\x12\x31\n\x05peers\x18\x01 \x03(\x0b\x32\".io.casperlabs.comm.discovery.Node2]\n\x0b\x44iagnostics\x12N\n\tListPeers\x12\x16.google.protobuf.Empty\x1a).io.casperlabs.node.api.diagnostics.Peersb\x06proto3')
  ,
  dependencies=[empty__pb2.DESCRIPTOR,node__pb2.DESCRIPTOR,])




_NODECOREMETRICS = _descriptor.Descriptor(
  name='NodeCoreMetrics',
  full_name='io.casperlabs.node.api.diagnostics.NodeCoreMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pingReceiverCount', full_name='io.casperlabs.node.api.diagnostics.NodeCoreMetrics.pingReceiverCount', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lookupReceiverCount', full_name='io.casperlabs.node.api.diagnostics.NodeCoreMetrics.lookupReceiverCount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disconnectReceiverCount', full_name='io.casperlabs.node.api.diagnostics.NodeCoreMetrics.disconnectReceiverCount', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connects', full_name='io.casperlabs.node.api.diagnostics.NodeCoreMetrics.connects', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p2pEncryptionHandshakeReceiverCount', full_name='io.casperlabs.node.api.diagnostics.NodeCoreMetrics.p2pEncryptionHandshakeReceiverCount', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p2pProtocolHandshakeReceiverCount', full_name='io.casperlabs.node.api.diagnostics.NodeCoreMetrics.p2pProtocolHandshakeReceiverCount', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peers', full_name='io.casperlabs.node.api.diagnostics.NodeCoreMetrics.peers', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from', full_name='io.casperlabs.node.api.diagnostics.NodeCoreMetrics.from', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='io.casperlabs.node.api.diagnostics.NodeCoreMetrics.to', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=336,
)


_PEERS = _descriptor.Descriptor(
  name='Peers',
  full_name='io.casperlabs.node.api.diagnostics.Peers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peers', full_name='io.casperlabs.node.api.diagnostics.Peers.peers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=396,
)

_PEERS.fields_by_name['peers'].message_type = node__pb2._NODE
DESCRIPTOR.message_types_by_name['NodeCoreMetrics'] = _NODECOREMETRICS
DESCRIPTOR.message_types_by_name['Peers'] = _PEERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeCoreMetrics = _reflection.GeneratedProtocolMessageType('NodeCoreMetrics', (_message.Message,), {
  'DESCRIPTOR' : _NODECOREMETRICS,
  '__module__' : 'diagnostics_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.node.api.diagnostics.NodeCoreMetrics)
  })
_sym_db.RegisterMessage(NodeCoreMetrics)

Peers = _reflection.GeneratedProtocolMessageType('Peers', (_message.Message,), {
  'DESCRIPTOR' : _PEERS,
  '__module__' : 'diagnostics_pb2'
  # @@protoc_insertion_point(class_scope:io.casperlabs.node.api.diagnostics.Peers)
  })
_sym_db.RegisterMessage(Peers)



_DIAGNOSTICS = _descriptor.ServiceDescriptor(
  name='Diagnostics',
  full_name='io.casperlabs.node.api.diagnostics.Diagnostics',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=398,
  serialized_end=491,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListPeers',
    full_name='io.casperlabs.node.api.diagnostics.Diagnostics.ListPeers',
    index=0,
    containing_service=None,
    input_type=empty__pb2._EMPTY,
    output_type=_PEERS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIAGNOSTICS)

DESCRIPTOR.services_by_name['Diagnostics'] = _DIAGNOSTICS

# @@protoc_insertion_point(module_scope)
