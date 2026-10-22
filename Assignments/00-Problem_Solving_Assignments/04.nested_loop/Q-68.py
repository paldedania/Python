# Q68. Number Border Pattern
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(n):
    line = ""
    for col in range(n):
        if line:
            line += ''
        line += str(1 if row == 0 or row == n - 1 or col == 0 or col == n - 1 else 0)
    print(line)
