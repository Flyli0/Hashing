from SHA256.SecureHashingAlgorithm import sha_256
from SHA256.Padding import padding
print(len(bin(padding("abc"))[2:]) % 512)
print(sha_256("abc").hex())
