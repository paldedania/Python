# Q13. Even-Odd Classification
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
# Outer loop selects a row; inner loop produces its columns.
for row in range(1, 5):
    line = ""
    for col in range(1, 5):
        if line:
            line += ' '
        line += str("E" if (row + col) % 2 == 0 else "O")
    print(line)
