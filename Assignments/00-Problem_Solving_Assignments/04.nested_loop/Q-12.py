# Q12. Odd Number Grid
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(n):
    line = ""
    for col in range(1, n + 1, 2):
        if line:
            line += ' '
        line += str(col)
    print(line)
