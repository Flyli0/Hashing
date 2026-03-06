from HMAC.HMAC import hmac
from SHA256.Constants import HASH_LENGTH
import math


def expand(output_length: int, info: str, prk: bytes):
    N = math.ceil(output_length / HASH_LENGTH)
    T = b""
    OKM = b""
    info = info.encode("utf-8")
    for i in range(1, N + 1):
        T = hmac(prk, T + info + bytes([i]))
        OKM += T
    return OKM[:output_length]
