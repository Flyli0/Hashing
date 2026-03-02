import math
from HMAC import hmac
from HMAC.Xor import xor
from SHA256.Constants import HASH_LENGTH

def pbkdf2(password: bytes, salt: bytes, iterations: int, key_length: int) -> bytes:
    l = math.ceil(key_length / HASH_LENGTH)
    derived_key = b''

    for i in range(1, l + 1):
        u = hmac(password, salt + i.to_bytes(4, 'big'))
        t = u

        for _ in range(1, iterations):
            u = hmac(password, u)
            t = xor(t, u)

        dk += t

    return dk[:key_length]