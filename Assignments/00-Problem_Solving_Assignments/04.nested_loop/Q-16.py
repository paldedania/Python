# Q16. Number Divisibility Grid
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
# Outer loop selects a row; inner loop produces its columns.
for row in range(1, 6):
    line = ""
    for col in range(1, 6):
        if line:
            line += ' '
        line += str("X" if row % col == 0 else "-")
    print(line)
