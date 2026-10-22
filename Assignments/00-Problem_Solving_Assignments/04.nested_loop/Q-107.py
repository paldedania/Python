# Q107. Number Triangle With Conditions
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
# E/O classify column values; X takes priority on the diagonal.
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(1, n + 1):
    line = ""
    for col in range(1, row + 1):
        if line:
            line += ' '
        line += str("X" if row == col else "E" if col % 2 == 0 else "O")
    print(line)
