# Q11. Even Number Grid
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows = int(input())
columns = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(rows):
    line = ""
    for col in range(2, columns + 1, 2):
        if line:
            line += ' '
        line += str(col)
    print(line)
