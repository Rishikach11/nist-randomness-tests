import os
import csv

def parse_result_file(filepath):
    features = []
    with open(filepath, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if '\tRandom' in line:
            features.append(1)
        elif '\tNon-Random' in line:
            features.append(0)
    return features

def generate_dataset():
    result_dir = 'sequences'
    output_file = 'dataset.csv'

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for filename in os.listdir(result_dir):
            if filename.startswith('result_random') and filename.endswith('.txt'):
                path = os.path.join(result_dir, filename)
                features = parse_result_file(path)
                features.append(1)  # Label: Random
                writer.writerow(features)

            elif filename.startswith('result_non_random') and filename.endswith('.txt'):
                path = os.path.join(result_dir, filename)
                features = parse_result_file(path)
                features.append(0)  # Label: Not Random
                writer.writerow(features)

if __name__ == '__main__':
    generate_dataset()
    print("✅ Dataset generated and saved as dataset.csv")
