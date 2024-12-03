import re

# Regex patterns
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
mul_pattern = r"mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"

with open("input.txt", "r") as file:
    data = file.read()  # Read the entire content of the file

# Initialize variables
take_mul = True  # Flag to determine if mul() results are valid
total_sum = 0

# Process the input
tokens = re.split(r"(do\(\)|don't\(\)|mul\(\s*-?\d+\s*,\s*-?\d+\s*\))", data)

for token in tokens:
    if re.fullmatch(do_pattern, token):
        take_mul = True
        print("Found: do(), enabling mul().")
    elif re.fullmatch(dont_pattern, token):
        take_mul = False
        print("Found: don't(), disabling mul().")
    elif re.fullmatch(mul_pattern, token) and take_mul:
        # Extract numbers from the valid mul() instruction
        match = re.match(mul_pattern, token)
        if match:
            number1, number2 = int(match[1]), int(match[2])
            result = number1 * number2
            total_sum += result
            print(f"Valid mul({number1},{number2}) -> {result}")

# Output the total sum
print(f"Total sum of valid mul() results: {total_sum}")
