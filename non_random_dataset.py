import os
import random

# Create folder if it doesn't exist
folder = "non_random_sequences"
os.makedirs(folder, exist_ok=True)

def write_sequence(filename, sequence):
    with open(os.path.join(folder, filename), "w") as f:
        f.write(sequence)

# 1. All 0s
write_sequence("not_random1_all_zeros.txt", "0" * 1000000)

# 2. All 1s
write_sequence("not_random2_all_ones.txt", "1" * 1000000)

# 3. Alternating 0s and 1s
write_sequence("not_random3_alternating.txt", "".join(["01"] * 500000))

# 4. Repeating block of 00001111
write_sequence("not_random4_blocks.txt", "00001111" * 125000)

# 5. Increasing density
sequence5 = ""
for _ in range(5):
    sequence5 += "0" * 100000 + "1" * 100000
write_sequence("not_random5_increasing_density.txt", sequence5[:1000000])

# 6. "HelloWorld" in ASCII repeated
binary_hello = ''.join([format(ord(c), '08b') for c in "HelloWorld"])
write_sequence("not_random6_ascii_helloworld.txt", (binary_hello * (1000000 // len(binary_hello)))[:1000000])

# 7. Fake Pi digits in binary (not actual pi)
fake_pi = "110010010000111111011010101000100010000110100011"  # just a random string
write_sequence("not_random7_fake_pi.txt", (fake_pi * (1000000 // len(fake_pi)))[:1000000])

# 8. Mostly 0s, 1s appear every 10,000 bits
sequence8 = ["0"] * 1000000
for i in range(0, 1000000, 10000):
    sequence8[i] = "1"
write_sequence("not_random8_sparse_ones.txt", "".join(sequence8))

# 9. One random block in the middle
middle_random = "".join(random.choices("01", k=100000))
sequence9 = "0" * 450000 + middle_random + "0" * 450000
write_sequence("not_random9_one_random_block.txt", sequence9[:1000000])

# 10. Shifted version of a repeating pattern
base_pattern = "00110101"
shifted = "".join(base_pattern[(i+1)%len(base_pattern)] for i in range(1000000))
write_sequence("not_random10_shifted_pattern.txt", shifted[:1000000])

print(f"✅ Generated 10 not-random sequences in '{folder}/'")
