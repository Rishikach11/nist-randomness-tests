import random
import numpy as np
import os
from scipy.stats import chisquare
import matplotlib.pyplot as plt

# Ensure output directory exists
if not os.path.exists("output"):
    os.makedirs("output")

# 1. Python's built-in random (Mersenne Twister)
def generate_python_random(n, filename="output/python_random.bin"):
    random.seed(42)  # For reproducibility
    with open(filename, "wb") as f:
        for _ in range(n):
            # Generate a random integer (0 or 1) for binary output
            f.write(int(random.random() >= 0.5).to_bytes(1, byteorder='big'))
    return filename

# 2. NumPy random number generator
def generate_numpy_random(n, filename="output/numpy_random.bin"):
    np.random.seed(42)  # For reproducibility
    random_bits = (np.random.random(n) >= 0.5).astype(np.uint8)
    with open(filename, "wb") as f:
        f.write(random_bits.tobytes())
    return filename

# 3. Linear Congruential Generator (LCG)
def generate_lcg(n, filename="output/lcg_random.bin"):
    # LCG parameters (similar to ANSI C rand())
    a = 1103515245
    c = 12345
    m = 2**31
    seed = 42
    x = seed
    with open(filename, "wb") as f:
        for _ in range(n):
            x = (a * x + c) % m
            # Convert to binary (0 or 1)
            bit = 1 if (x / m) >= 0.5 else 0
            f.write(bit.to_bytes(1, byteorder='big'))
    return filename

# Generate 1MB of random data for each method
n_bytes = 1_000_000
print("Generating random sequences...")
python_file = generate_python_random(n_bytes)
numpy_file = generate_numpy_random(n_bytes)
lcg_file = generate_lcg(n_bytes)
print(f"Generated files: {python_file}, {numpy_file}, {lcg_file}")


def frequency_test(filename):
    """Perform a frequency (monobit) test on binary data."""
    with open(filename, "rb") as f:
        data = f.read()
    bits = [int(b) for b in data]
    n_ones = sum(bits)
    n_zeros = len(bits) - n_ones
    # Expected counts for random data
    expected = [len(bits) / 2, len(bits) / 2]
    observed = [n_ones, n_zeros]
    chi2, p_value = chisquare(observed, expected)
    return {"chi2": chi2, "p_value": p_value, "pass": p_value >= 0.01}

def runs_test(filename):
    """Perform a runs test on binary data."""
    with open(filename, "rb") as f:
        data = f.read()
    bits = [int(b) for b in data]
    runs = 1
    for i in range(1, len(bits)):
        if bits[i] != bits[i-1]:
            runs += 1
    n = len(bits)
    n1 = sum(bits)
    n0 = n - n1
    if n0 == 0 or n1 == 0:
        return {"runs": runs, "p_value": 0, "pass": False}
    # Expected number of runs and variance
    expected_runs = (2 * n0 * n1) / n + 1
    variance = (2 * n0 * n1 * (2 * n0 * n1 - n)) / (n**2 * (n - 1))
    z = (runs - expected_runs) / (variance**0.5)
    from scipy.stats import norm
    p_value = 2 * (1 - norm.cdf(abs(z)))
    return {"runs": runs, "z_score": z, "p_value": p_value, "pass": p_value >= 0.01}

# Run tests on generated files
files = [python_file, numpy_file, lcg_file]
for file in files:
    print(f"\nTesting {file}:")
    freq_result = frequency_test(file)
    runs_result = runs_test(file)
    print(f"Frequency Test: chi2={freq_result['chi2']:.2f}, p-value={freq_result['p_value']:.4f}, Pass={freq_result['pass']}")
    print(f"Runs Test: z-score={runs_result['z_score']:.2f}, p-value={runs_result['p_value']:.4f}, Pass={runs_result['pass']}")