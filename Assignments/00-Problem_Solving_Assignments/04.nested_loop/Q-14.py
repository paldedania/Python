# Q14. Equal Coordinate Detector
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
# The sample uses N=3; accept N rather than fixing it at 5.
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(n):
    line = ""
    for col in range(n):
        if line:
            line += ' '
        line += str("Same" if row == col else "Different")
    print(line)
