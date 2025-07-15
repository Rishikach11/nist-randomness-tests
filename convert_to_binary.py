with open("random_bits.txt", "r") as txt_file:
    bits = txt_file.read().strip()

with open("random_bits.bin", "wb") as bin_file:
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            byte = byte.ljust(8, '0')  # pad with 0s if not full 8 bits
        bin_file.write(bytes([int(byte, 2)]))
