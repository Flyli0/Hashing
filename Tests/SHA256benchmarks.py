from SHA256.SecureHashingAlgorithm import sha_256
import time

data = b"a" * (10 * 1024 * 1024)  # there are 100 megabytes of an 'a' symbols

start = time.perf_counter()
digest = sha_256(data)
end = time.perf_counter()

time = end - start
mbs = 10/time

print(f"time taken: {time}")
print(f"speed: {mbs} MB/s")
