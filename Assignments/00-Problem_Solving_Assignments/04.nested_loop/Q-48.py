# Q48. Reverse Dynamic Range
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(1, n + 1):
    line = ""
    for col in range(row, 0, -1):
        if line:
            line += ' '
        line += str(col)
    print(line)
