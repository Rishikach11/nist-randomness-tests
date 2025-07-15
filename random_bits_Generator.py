import random

with open("random_bits.txt", "w") as f:
    for _ in range(1000000):  # 10 lakh bits
        f.write(str(random.randint(0, 1)))
