# clean_dataset.py
cleaned = []
with open('dataset.csv', 'r') as f:
    for line in f:
        fields = line.strip().split(',')
        if len(fields) == 34:
            cleaned.append(','.join(fields))

with open('dataset_cleaned.csv', 'w') as f:
    f.write('\n'.join(cleaned))

print("✅ Cleaned dataset saved to 'dataset_cleaned.csv'")
