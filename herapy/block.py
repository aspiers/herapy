# -*- coding: utf-8 -*-

import base58

from google.protobuf.json_format import MessageToJson


class Block:
    def __init__(self, hash_value=None, height=None):
        if isinstance(hash_value, str):
            hash_value = base58.b58decode_check(hash_value)

        self.__info = None
        self.__hash = hash_value
        # header
        self.__prev_block = None
        self.__block_no = height
        self.__timestamp = None
        self.__blocks_root_hash = None
        self.__txs_root_hash = None
        self.__confirms = None
        self.__public_key = None
        self.__sign = None
        # body
        self.__body = None

    @property
    def info(self):
        return MessageToJson(self.__info)

    @info.setter
    def info(self, v):
        self.__info = v
        self.__hash = v.hash
        # header
        header = v.header
        self.__prev_block = Block(hash_value=header.prevBlockHash,
                                  height=header.blockNo - 1)
        self.__block_no = header.blockNo
        self.__timestamp = header.timestamp
        self.__blocks_root_hash = header.blocksRootHash
        self.__txs_root_hash = header.txsRootHash
        self.__confirms = header.confirms
        self.__public_key = header.pubKey
        self.__sign = header.sign
        # body
        self.__body = v.body

    @property
    def hash(self):
        return base58.b58encode_check(self.__hash)

    @property
    def height(self):
        return self.__block_no

    @property
    def prev(self):
        return self.__prev_block

    @property
    def block_no(self):
        return self.__block_no

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def blocks_root_hash(self):
        return self.__blocks_root_hash

    @property
    def txs_root_hash(self):
        return self.__txs_root_hash

    @property
    def confirms(self):
        return self.__confirms

    @property
    def public_key(self):
        return self.__public_key

    @property
    def sign(self):
        return self.__sign

    @property
    def body(self):
        return self.__body

    @staticmethod
    def encode_block_hash(block_hash):
        return base58.b58encode_check(block_hash)

    @staticmethod
    def decode_block_hash(block_hash):
        return base58.b58decode_check(block_hash)