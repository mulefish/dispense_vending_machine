import sys

def process_input():
    for line in sys.stdin:
        line = line.strip()  # Remove leading/trailing whitespace

        # Check if the line is not null (empty) and is longer than 3 characters
        if line and len(line) > 3:
            print(f"Valid input: {line}")
        else:
            print("Invalid input. Input should be longer than 3 characters and not empty.")

if __name__ == "__main__":
    process_input()