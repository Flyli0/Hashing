import math
from HMAC.HMAC import hmac
from HMAC.Xor import xor
from SHA256.Constants import HASH_LENGTH

# function that takes password, salt, number of iterations and key length (key
# length is number of bytes in key) and returns first key length bytes of derived 
# key
def pbkdf2(password: bytes, salt: bytes, iterations: int, key_length: int) -> bytes:
    l = math.ceil(key_length / HASH_LENGTH)
    dk = b''

    for i in range(1, l + 1):
        u = hmac(password, salt + i.to_bytes(4, 'big'))
        t = u

        for _ in range(1, iterations):
            u = hmac(password, u)
            t = xor(t, u)

        dk += t

    return dk[:key_length]
