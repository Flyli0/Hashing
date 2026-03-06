from SHA256.SecureHashingAlgorithm import sha_256
from SHA256.Padding import padding
from HMAC.HMAC import hmac
a = "abc"
a = a.encode("utf-8")
print(sha_256(a).hex())
key = bytes.fromhex("0b" * 20)
message = b"Hi There"
print(hmac(key,message).hex())
