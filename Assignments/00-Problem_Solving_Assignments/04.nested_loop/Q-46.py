# Q46. Conditional Dynamic Loop
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(1, n + 1):
    line = ""
    for col in range(2, row + 1, 2):
        if line:
            line += ' '
        line += str(col)
    print(line)
