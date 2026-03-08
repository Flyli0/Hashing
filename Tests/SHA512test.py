from SHA512.SecureHashingAlgorithm import sha_512
import hashlib

print(hashlib.sha512(b"abc").hexdigest())
print(sha_512(b"abc").hex())