def analyze_nist_results(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    random_count = 0
    non_random_count = 0

    for line in lines:
        if 'Conclusion' in line:
            continue
        if 'Random' in line:
            if 'Non-Random' in line:
                non_random_count += 1
            else:
                random_count += 1

    total_tests = random_count + non_random_count

    print(f"Total Tests Evaluated: {total_tests}")
    print(f"Random: {random_count}")
    print(f"Non-Random: {non_random_count}")

    if total_tests == 0:
        print("No tests found in the file.")
        return

    if non_random_count == 0:
        print("Final Verdict: The sequence is RANDOM (100% tests passed)")
    elif random_count == 0:
        print("Final Verdict: The sequence is NON-RANDOM (0% tests passed)")
    elif random_count / total_tests >= 0.9:
        print(f"Final Verdict: The sequence is LIKELY RANDOM ({random_count}/{total_tests} tests passed)")
    else:
        print(f"Final Verdict: The sequence is NON-RANDOM ({random_count}/{total_tests} tests passed)")


# Example usage:
analyze_nist_results("semi_random_result.txt")
