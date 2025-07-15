import random
import os

os.makedirs("sequences", exist_ok=True)

def write_random(name, length=100000):
    bits = ''.join(str(random.getrandbits(1)) for _ in range(length))
    with open(f"sequences/{name}.txt", "w") as f:
        f.write(bits)

def write_not_random(name, length=100000):
    # Half 1s then half 0s
    bits = '1' * (length // 2) + '0' * (length // 2)
    with open(f"sequences/{name}.txt", "w") as f:
        f.write(bits)

# Generate 10 random + 10 not-random files
for i in range(10):
    write_random(f"random_{i}")
    write_not_random(f"not_random_{i}")
