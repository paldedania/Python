# Q47. Dynamic Range Based on Input
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(n):
    line = ""
    for col in range(row):
        if line:
            line += ' '
        line += str(col)
    print(line)
