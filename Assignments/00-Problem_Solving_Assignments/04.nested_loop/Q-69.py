# Q69. Diagonal Cross
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(n):
    line = ""
    for col in range(n):
        if line:
            line += ''
        line += str("*" if row == col or row + col == n - 1 else " ")
    print(line)
