cleaned_lines = []

with open("dataset.csv", "r") as infile:
    for i, line in enumerate(infile, 1):
        values = line.strip().split(",")
        if len(values) == 33:
            cleaned_lines.append(line)
        else:
            print(f"Skipping line {i}, had {len(values)} values")

with open("dataset_cleaned.csv", "w") as outfile:
    outfile.writelines(cleaned_lines)

print("✅ Cleaned dataset saved as dataset_cleaned.csv")
