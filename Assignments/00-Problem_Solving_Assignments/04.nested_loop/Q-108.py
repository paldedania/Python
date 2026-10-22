# Q108. Multiplication Pattern Challenge
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(1, n + 1):
    line = ""
    for col in range(1, n + 1):
        if line:
            line += ' '
        line += str("Z" if row * col % 15 == 0 else "X" if row * col % 3 == 0 else "Y" if row * col % 5 == 0 else row * col)
    print(line)
