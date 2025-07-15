import random

with open("semi_random.txt", "w") as f:
    bits = ""
    for i in range(10000):
        if i % 1000 < 500:
            bits += str(random.randint(0, 1))  # Random part
        else:
            bits += "0"  # Pattern
    f.write(bits)
