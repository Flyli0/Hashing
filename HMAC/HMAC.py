from SHA256.SecureHashingAlgorithm import sha_256
from SHA256.Constants import BLOCK_SIZE
from SHA256.Constants import opad
from SHA256.Constants import ipad
from Xor import xor

def hmac_sha256(key, message):

    if len(key) > BLOCK_SIZE:
        key = sha_256(key)

    if len(key) < BLOCK_SIZE:
        key = key + b'\x00' * (BLOCK_SIZE - len(key))
    
    inner_key = xor(key, ipad)
    inner_hash = sha_256(inner_key + message)

    outer_key = xor(key, opad)
    hmac = sha_256(outer_key + inner_hash)

    return hmac