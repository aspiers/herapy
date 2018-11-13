# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blockchain.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='blockchain.proto',
  package='types',
  syntax='proto3',
  serialized_options=_b('Z\036github.com/aergoio/aergo/types'),
  serialized_pb=_b('\n\x10\x62lockchain.proto\x12\x05types\"Y\n\x05\x42lock\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\"\n\x06header\x18\x02 \x01(\x0b\x32\x12.types.BlockHeader\x12\x1e\n\x04\x62ody\x18\x03 \x01(\x0b\x32\x10.types.BlockBody\"\xd8\x01\n\x0b\x42lockHeader\x12\x15\n\rprevBlockHash\x18\x01 \x01(\x0c\x12\x0f\n\x07\x62lockNo\x18\x02 \x01(\x04\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x16\n\x0e\x62locksRootHash\x18\x04 \x01(\x0c\x12\x13\n\x0btxsRootHash\x18\x05 \x01(\x0c\x12\x18\n\x10receiptsRootHash\x18\x06 \x01(\x0c\x12\x10\n\x08\x63onfirms\x18\x07 \x01(\x04\x12\x0e\n\x06pubKey\x18\x08 \x01(\x0c\x12\x0c\n\x04sign\x18\t \x01(\x0c\x12\x17\n\x0f\x63oinbaseAccount\x18\n \x01(\x0c\"#\n\tBlockBody\x12\x16\n\x03txs\x18\x01 \x03(\x0b\x32\t.types.Tx\" \n\x06TxList\x12\x16\n\x03txs\x18\x01 \x03(\x0b\x32\t.types.Tx\"/\n\x02Tx\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x1b\n\x04\x62ody\x18\x02 \x01(\x0b\x32\r.types.TxBody\"\xa5\x01\n\x06TxBody\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x0f\n\x07\x61\x63\x63ount\x18\x02 \x01(\x0c\x12\x11\n\trecipient\x18\x03 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12\x0f\n\x07payload\x18\x05 \x01(\x0c\x12\r\n\x05limit\x18\x06 \x01(\x04\x12\r\n\x05price\x18\x07 \x01(\x04\x12\x1b\n\x04type\x18\x08 \x01(\x0e\x32\r.types.TxType\x12\x0c\n\x04sign\x18\t \x01(\x0c\"\'\n\x05TxIdx\x12\x11\n\tblockHash\x18\x01 \x01(\x0c\x12\x0b\n\x03idx\x18\x02 \x01(\x05\"?\n\tTxInBlock\x12\x1b\n\x05txIdx\x18\x01 \x01(\x0b\x32\x0c.types.TxIdx\x12\x15\n\x02tx\x18\x02 \x01(\x0b\x32\t.types.Tx\"h\n\x05State\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x0f\n\x07\x62\x61lance\x18\x02 \x01(\x04\x12\x10\n\x08\x63odeHash\x18\x03 \x01(\x0c\x12\x13\n\x0bstorageRoot\x18\x04 \x01(\x0c\x12\x18\n\x10sqlRecoveryPoint\x18\x05 \x01(\x04\"\x93\x01\n\nStateProof\x12\x1b\n\x05State\x18\x01 \x01(\x0b\x32\x0c.types.State\x12\x11\n\tinclusion\x18\x02 \x01(\x08\x12\x10\n\x08proofKey\x18\x03 \x01(\x0c\x12\x10\n\x08proofVal\x18\x04 \x01(\x0c\x12\x0e\n\x06\x62itmap\x18\x05 \x01(\x0c\x12\x0e\n\x06height\x18\x06 \x01(\r\x12\x11\n\tauditPath\x18\x07 \x03(\x0c\"?\n\x07Receipt\x12\x17\n\x0f\x63ontractAddress\x18\x01 \x01(\x0c\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0b\n\x03ret\x18\x03 \x01(\t\"\x1a\n\nFnArgument\x12\x0c\n\x04name\x18\x01 \x01(\t\">\n\x08\x46unction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\targuments\x18\x02 \x03(\x0b\x32\x11.types.FnArgument\"L\n\x03\x41\x42I\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\"\n\tfunctions\x18\x03 \x03(\x0b\x32\x0f.types.Function\"3\n\x05Query\x12\x17\n\x0f\x63ontractAddress\x18\x01 \x01(\x0c\x12\x11\n\tqueryinfo\x18\x02 \x01(\x0c*$\n\x06TxType\x12\n\n\x06NORMAL\x10\x00\x12\x0e\n\nGOVERNANCE\x10\x01\x42 Z\x1egithub.com/aergoio/aergo/typesb\x06proto3')
)

_TXTYPE = _descriptor.EnumDescriptor(
  name='TxType',
  full_name='types.TxType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOVERNANCE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1275,
  serialized_end=1311,
)
_sym_db.RegisterEnumDescriptor(_TXTYPE)

TxType = enum_type_wrapper.EnumTypeWrapper(_TXTYPE)
NORMAL = 0
GOVERNANCE = 1



_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='types.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='types.Block.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='types.Block.header', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='types.Block.body', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=27,
  serialized_end=116,
)


_BLOCKHEADER = _descriptor.Descriptor(
  name='BlockHeader',
  full_name='types.BlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prevBlockHash', full_name='types.BlockHeader.prevBlockHash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blockNo', full_name='types.BlockHeader.blockNo', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='types.BlockHeader.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blocksRootHash', full_name='types.BlockHeader.blocksRootHash', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txsRootHash', full_name='types.BlockHeader.txsRootHash', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiptsRootHash', full_name='types.BlockHeader.receiptsRootHash', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirms', full_name='types.BlockHeader.confirms', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pubKey', full_name='types.BlockHeader.pubKey', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sign', full_name='types.BlockHeader.sign', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coinbaseAccount', full_name='types.BlockHeader.coinbaseAccount', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=119,
  serialized_end=335,
)


_BLOCKBODY = _descriptor.Descriptor(
  name='BlockBody',
  full_name='types.BlockBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txs', full_name='types.BlockBody.txs', index=0,
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
  serialized_start=337,
  serialized_end=372,
)


_TXLIST = _descriptor.Descriptor(
  name='TxList',
  full_name='types.TxList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txs', full_name='types.TxList.txs', index=0,
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
  serialized_start=374,
  serialized_end=406,
)


_TX = _descriptor.Descriptor(
  name='Tx',
  full_name='types.Tx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='types.Tx.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='types.Tx.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=408,
  serialized_end=455,
)


_TXBODY = _descriptor.Descriptor(
  name='TxBody',
  full_name='types.TxBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='types.TxBody.nonce', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account', full_name='types.TxBody.account', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='types.TxBody.recipient', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='types.TxBody.amount', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='types.TxBody.payload', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='types.TxBody.limit', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='types.TxBody.price', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='types.TxBody.type', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sign', full_name='types.TxBody.sign', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=458,
  serialized_end=623,
)


_TXIDX = _descriptor.Descriptor(
  name='TxIdx',
  full_name='types.TxIdx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blockHash', full_name='types.TxIdx.blockHash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='idx', full_name='types.TxIdx.idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=625,
  serialized_end=664,
)


_TXINBLOCK = _descriptor.Descriptor(
  name='TxInBlock',
  full_name='types.TxInBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txIdx', full_name='types.TxInBlock.txIdx', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx', full_name='types.TxInBlock.tx', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=666,
  serialized_end=729,
)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='types.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='types.State.nonce', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance', full_name='types.State.balance', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeHash', full_name='types.State.codeHash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storageRoot', full_name='types.State.storageRoot', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sqlRecoveryPoint', full_name='types.State.sqlRecoveryPoint', index=4,
      number=5, type=4, cpp_type=4, label=1,
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
  serialized_start=731,
  serialized_end=835,
)


_STATEPROOF = _descriptor.Descriptor(
  name='StateProof',
  full_name='types.StateProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='State', full_name='types.StateProof.State', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inclusion', full_name='types.StateProof.inclusion', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proofKey', full_name='types.StateProof.proofKey', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proofVal', full_name='types.StateProof.proofVal', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bitmap', full_name='types.StateProof.bitmap', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='types.StateProof.height', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auditPath', full_name='types.StateProof.auditPath', index=6,
      number=7, type=12, cpp_type=9, label=3,
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
  serialized_start=838,
  serialized_end=985,
)


_RECEIPT = _descriptor.Descriptor(
  name='Receipt',
  full_name='types.Receipt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contractAddress', full_name='types.Receipt.contractAddress', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='types.Receipt.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ret', full_name='types.Receipt.ret', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=987,
  serialized_end=1050,
)


_FNARGUMENT = _descriptor.Descriptor(
  name='FnArgument',
  full_name='types.FnArgument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='types.FnArgument.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1052,
  serialized_end=1078,
)


_FUNCTION = _descriptor.Descriptor(
  name='Function',
  full_name='types.Function',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='types.Function.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='types.Function.arguments', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1080,
  serialized_end=1142,
)


_ABI = _descriptor.Descriptor(
  name='ABI',
  full_name='types.ABI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='types.ABI.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='types.ABI.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functions', full_name='types.ABI.functions', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=1144,
  serialized_end=1220,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='types.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contractAddress', full_name='types.Query.contractAddress', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queryinfo', full_name='types.Query.queryinfo', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1222,
  serialized_end=1273,
)

_BLOCK.fields_by_name['header'].message_type = _BLOCKHEADER
_BLOCK.fields_by_name['body'].message_type = _BLOCKBODY
_BLOCKBODY.fields_by_name['txs'].message_type = _TX
_TXLIST.fields_by_name['txs'].message_type = _TX
_TX.fields_by_name['body'].message_type = _TXBODY
_TXBODY.fields_by_name['type'].enum_type = _TXTYPE
_TXINBLOCK.fields_by_name['txIdx'].message_type = _TXIDX
_TXINBLOCK.fields_by_name['tx'].message_type = _TX
_STATEPROOF.fields_by_name['State'].message_type = _STATE
_FUNCTION.fields_by_name['arguments'].message_type = _FNARGUMENT
_ABI.fields_by_name['functions'].message_type = _FUNCTION
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['BlockHeader'] = _BLOCKHEADER
DESCRIPTOR.message_types_by_name['BlockBody'] = _BLOCKBODY
DESCRIPTOR.message_types_by_name['TxList'] = _TXLIST
DESCRIPTOR.message_types_by_name['Tx'] = _TX
DESCRIPTOR.message_types_by_name['TxBody'] = _TXBODY
DESCRIPTOR.message_types_by_name['TxIdx'] = _TXIDX
DESCRIPTOR.message_types_by_name['TxInBlock'] = _TXINBLOCK
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['StateProof'] = _STATEPROOF
DESCRIPTOR.message_types_by_name['Receipt'] = _RECEIPT
DESCRIPTOR.message_types_by_name['FnArgument'] = _FNARGUMENT
DESCRIPTOR.message_types_by_name['Function'] = _FUNCTION
DESCRIPTOR.message_types_by_name['ABI'] = _ABI
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.enum_types_by_name['TxType'] = _TXTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.Block)
  ))
_sym_db.RegisterMessage(Block)

BlockHeader = _reflection.GeneratedProtocolMessageType('BlockHeader', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKHEADER,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.BlockHeader)
  ))
_sym_db.RegisterMessage(BlockHeader)

BlockBody = _reflection.GeneratedProtocolMessageType('BlockBody', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKBODY,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.BlockBody)
  ))
_sym_db.RegisterMessage(BlockBody)

TxList = _reflection.GeneratedProtocolMessageType('TxList', (_message.Message,), dict(
  DESCRIPTOR = _TXLIST,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.TxList)
  ))
_sym_db.RegisterMessage(TxList)

Tx = _reflection.GeneratedProtocolMessageType('Tx', (_message.Message,), dict(
  DESCRIPTOR = _TX,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.Tx)
  ))
_sym_db.RegisterMessage(Tx)

TxBody = _reflection.GeneratedProtocolMessageType('TxBody', (_message.Message,), dict(
  DESCRIPTOR = _TXBODY,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.TxBody)
  ))
_sym_db.RegisterMessage(TxBody)

TxIdx = _reflection.GeneratedProtocolMessageType('TxIdx', (_message.Message,), dict(
  DESCRIPTOR = _TXIDX,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.TxIdx)
  ))
_sym_db.RegisterMessage(TxIdx)

TxInBlock = _reflection.GeneratedProtocolMessageType('TxInBlock', (_message.Message,), dict(
  DESCRIPTOR = _TXINBLOCK,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.TxInBlock)
  ))
_sym_db.RegisterMessage(TxInBlock)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(
  DESCRIPTOR = _STATE,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.State)
  ))
_sym_db.RegisterMessage(State)

StateProof = _reflection.GeneratedProtocolMessageType('StateProof', (_message.Message,), dict(
  DESCRIPTOR = _STATEPROOF,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.StateProof)
  ))
_sym_db.RegisterMessage(StateProof)

Receipt = _reflection.GeneratedProtocolMessageType('Receipt', (_message.Message,), dict(
  DESCRIPTOR = _RECEIPT,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.Receipt)
  ))
_sym_db.RegisterMessage(Receipt)

FnArgument = _reflection.GeneratedProtocolMessageType('FnArgument', (_message.Message,), dict(
  DESCRIPTOR = _FNARGUMENT,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.FnArgument)
  ))
_sym_db.RegisterMessage(FnArgument)

Function = _reflection.GeneratedProtocolMessageType('Function', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTION,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.Function)
  ))
_sym_db.RegisterMessage(Function)

ABI = _reflection.GeneratedProtocolMessageType('ABI', (_message.Message,), dict(
  DESCRIPTOR = _ABI,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.ABI)
  ))
_sym_db.RegisterMessage(ABI)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(
  DESCRIPTOR = _QUERY,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:types.Query)
  ))
_sym_db.RegisterMessage(Query)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
