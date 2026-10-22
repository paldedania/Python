# Q60. Inverted Triangle
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(n, 0, -1):
    line = ""
    for col in range(row):
        if line:
            line += ''
        line += str("*")
    print(line)
