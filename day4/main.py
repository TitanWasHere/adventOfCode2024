# Nome del file
file_name = "input.txt"

# Legge il file e lo salva come matrice
with open(file_name, 'r') as file:
    matrix = [list(line.strip().replace(" ", "")) for line in file]

word = "XMAS"

def check_word(matrix, i, j, direction):
    x = []
    for k in range(0, len(word)):
        new_i = i + k * direction[0]
        new_j = j + k * direction[1]
        if new_i < 0 or new_i >= len(matrix) or new_j < 0 or new_j >= len(matrix[new_i]):
            return 0
        if matrix[new_i][new_j] != word[k]:
            return 0
        x.append((new_i, new_j))
    print(x)
    return 1

def check_direction(matrix, i, j):
    tot = 0
    for direction in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        tot += check_word(matrix, i, j, direction)

    return tot

def check_start(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            count += check_direction(matrix, i, j)
    return count
def part1():
    return check_start(matrix)

def check_MAS(matrix, i, j):
    # Check bounds to avoid index errors
    if i + 2 >= len(matrix) or j + 2 >= len(matrix[0]):
        return 0

    # Extract relevant characters for comparison
    top_left = matrix[i][j]
    top_right = matrix[i][j+2]
    center = matrix[i+1][j+1]
    bottom_left = matrix[i+2][j]
    bottom_right = matrix[i+2][j+2]
    # Center must always be 'A'
    if center != "A":
        return 0
    
    accepted_chars = ["M", "S"]
    if top_left not in accepted_chars or top_right not in accepted_chars or bottom_left not in accepted_chars or bottom_right not in accepted_chars:
        return 0
    if (top_left == top_right and bottom_left == bottom_right and top_left != bottom_left):
        return 1
    elif(top_left == bottom_right and top_right == bottom_left and top_left != top_right):
        return 1
    elif(top_left == bottom_left and top_right == bottom_right and top_left != top_right):
        return 1

    return 0

def check_word2(matrix):
    tot = 0
    for i in range(len(matrix) - 2):  # Stop at len(matrix)-2 for safe bounds
        for j in range(len(matrix[i]) - 2):  # Stop at len(matrix[i])-2 for safe bounds
            tot += check_MAS(matrix, i, j)

    return tot

def part2(matrix):
    return check_word2(matrix)

#print(part1())
print(part2(matrix))
