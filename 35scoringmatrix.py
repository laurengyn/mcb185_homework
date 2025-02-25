import sys

alphabet = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

letters = list(alphabet)
matrix = []

for i in range(0, len(letters)):
    row = []
    for j in range(0, len(letters)):
        if letters[i] == letters[j]:
            row.append(match)
        else:
            row.append(mismatch)
    matrix.append(row)

# printing header
print('     ', end='')
for  base in letters:
    print(f" {base}", end='')
print()

# printing rows
for i in range(0, len(letters)):
    print(f'{letters[i]} ', end='')
    for j in range(0, len(letters)):
        print(f' {matrix[i][j]}', end='')
    print()