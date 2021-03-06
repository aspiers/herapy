# -*- coding: utf-8 -*-

"""Common utility module for converting types."""

import hashlib
import json
import toml
import socket
import ecdsa
import time
from typing import (
    Union,
)

from ..obj.aergo_conf import AergoConfig
from ..grpc import blockchain_pb2
from ..constants import (
    PUBLIC_KEY_UNCOMPRESSED,
    PUBLIC_KEY_COMPRESSED_E,
    PUBLIC_KEY_COMPRESSED_O
)
from .encoding import (
    encode_b58,
    encode_address
)


def convert_toml_to_aergo_conf(v: str) -> AergoConfig:
    aergo_conf = AergoConfig()

    conf = toml.loads(v)
    for k, v in conf.items():
        if isinstance(v, dict):
            for k2, v2 in v.items():
                aergo_conf.add_conf(k2, v2, k)
        else:
            aergo_conf.add_conf(k, v)

    return aergo_conf


def convert_aergo_conf_to_toml(aergo_conf: AergoConfig) -> str:
    return toml.dumps(aergo_conf.conf)


def convert_tx_to_grpc_tx(tx):
    grpc_tx = blockchain_pb2.Tx()
    grpc_tx.hash = bytes(tx.tx_hash)
    if tx.nonce is not None:
        grpc_tx.body.nonce = tx.nonce
    if tx.from_address is not None:
        grpc_tx.body.account = bytes(tx.from_address)
    if tx.to_address is not None:
        grpc_tx.body.recipient = bytes(tx.to_address)
    if tx.amount is not None:
        grpc_tx.body.amount = bytes(tx.amount)
    if tx.payload is not None:
        grpc_tx.body.payload = tx.payload
    grpc_tx.body.gasLimit = tx.gas_limit
    grpc_tx.body.gasPrice = bytes(tx.gas_price)
    grpc_tx.body.type = tx.tx_type.value
    grpc_tx.body.chainIdHash = tx.chain_id
    if tx.sign is not None:
        grpc_tx.body.sign = tx.sign
    return grpc_tx


def tx_to_grpc_tx(v):
    return convert_tx_to_grpc_tx(v)


def convert_tx_to_json(tx):
    if tx is None:
        return None

    return tx.json()


def tx_to_json(v):
    return convert_tx_to_json(v)


def convert_tx_to_formatted_json(tx):
    if tx is None:
        return None
    return json.dumps(convert_tx_to_json(tx), indent=2)


def tx_to_formatted_json(v):
    return convert_tx_to_formatted_json(v)


def convert_bytes_to_int_str(v):
    return ''.join('{:d} '.format(x) for x in v)


def bytes_to_int_str(v):
    return convert_bytes_to_int_str(v)


def convert_bytes_to_hex_str(v):
    return ''.join('0x{:02x} '.format(x) for x in v)


def convert_ip_bytes_to_str(ip):
    if isinstance(ip, str):
        return ip

    # IPv4
    if 4 == len(ip):
        return socket.inet_ntoa(ip)
    elif 16 == len(ip) and all(v2 == 0 for v2 in list(ip[:10])) \
            and 255 == ip[10] and 255 == ip[11]:
        return socket.inet_ntoa(ip[12:16])

    # IPv6
    return socket.inet_ntop(socket.AF_INET6, ip)


def convert_bigint_to_bytes(number: int) -> bytes:
    q, r = divmod(len(bin(number)) - 2, 8)
    bytes_to_fit_number = q if r == 0 else q + 1
    return number.to_bytes(bytes_to_fit_number, 'big')


def bigint_to_bytes(v: int) -> bytes:
    return convert_bigint_to_bytes(v)


def convert_public_key_to_bytes(
    pubkey,
    curve=ecdsa.SECP256k1,
    compressed=True
) -> bytes:
    if not isinstance(pubkey, ecdsa.ecdsa.Public_key):
        raise TypeError('value is not a valid public key')

    x = pubkey.point.x()
    x_bytes = ecdsa.util.number_to_string(x, curve.order)

    y = pubkey.point.y()
    if compressed:
        if y % 2 == 0:
            head = PUBLIC_KEY_COMPRESSED_E
        else:
            head = PUBLIC_KEY_COMPRESSED_O
        y_bytes = b''
    else:
        head = PUBLIC_KEY_UNCOMPRESSED
        y_bytes = ecdsa.util.number_to_string(y, curve.order)

    return head + x_bytes + y_bytes


def public_key_to_bytes(pubkey, curve=ecdsa.SECP256k1, compressed=True):
    return convert_public_key_to_bytes(pubkey=pubkey,
                                       curve=curve,
                                       compressed=compressed)


def convert_bytes_to_public_key(
    v: bytes,
    curve: ecdsa.curves.Curve = ecdsa.SECP256k1
) -> ecdsa.ecdsa.Public_key:
    if not isinstance(v, bytes):
        raise TypeError('value is not bytes')

    head = v[:1]
    if head not in (PUBLIC_KEY_UNCOMPRESSED,
                    PUBLIC_KEY_COMPRESSED_O,
                    PUBLIC_KEY_COMPRESSED_E):
        # can be a smart contract address, so no error
        raise ValueError("public key is not proper")

    x_bytes = v[1:curve.baselen + 1]
    x = ecdsa.util.string_to_number(x_bytes)

    if PUBLIC_KEY_UNCOMPRESSED == head:
        y_bytes = v[curve.baselen + 1:]
        y = ecdsa.util.string_to_number(y_bytes)
    else:
        a = curve.curve.a()
        b = curve.curve.b()
        p = curve.curve.p()

        if ecdsa.SECP256k1 == curve:
            # source: https://stackoverflow.com/questions/43629265/
            # deriving-an-ecdsa-uncompressed-public-key-from-a-compressed-one?rq=1
            y_square = (pow(x, 3, p) + a * x + b) % p
            y_square_square_root = pow(y_square, (p + 1) // 4, p)
            if ((head == PUBLIC_KEY_COMPRESSED_E
                 and y_square_square_root & 1)
                    or (head == PUBLIC_KEY_COMPRESSED_O
                        and not y_square_square_root & 1)):
                y = (-y_square_square_root) % p
            else:
                y = y_square_square_root
        else:
            # if supporting more formula, need to implement
            assert 1 == 0

    point = ecdsa.ellipticcurve.Point(curve.curve, x, y, curve.order)
    return ecdsa.ecdsa.Public_key(curve.generator, point)


def bytes_to_public_key(v, curve=ecdsa.SECP256k1):
    return convert_bytes_to_public_key(v, curve=curve)


def get_hash(
    *strings,
    no_rand: bool = False,
    no_encode: bool = False
) -> Union[str, bytes, None]:
    m = hashlib.sha256()
    if not no_rand:
        m.update(int(time.time()).to_bytes(8, 'little'))
    for string in strings:
        if isinstance(string, str):
            string = string.encode('utf-8')
        m.update(string)

    if no_encode:
        return m.digest()

    return encode_b58(m.digest())


def privkey_to_address(
    privkey: bytes,
    curve: ecdsa.curves.Curve = ecdsa.SECP256k1,
    compressed: bool = True
) -> str:
    d = int.from_bytes(privkey, byteorder='big')
    pubkey_point = curve.generator * d
    pubkey = ecdsa.ecdsa.Public_key(curve.generator, pubkey_point)
    pubkey_bytes = convert_public_key_to_bytes(pubkey, curve, compressed)
    return encode_address(pubkey_bytes)
