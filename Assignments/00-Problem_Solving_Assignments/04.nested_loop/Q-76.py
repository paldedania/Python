# Q76. Mini Seating System
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows = int(input())
columns = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(rows):
    line = ""
    for col in range(1, columns + 1):
        if line:
            line += ' '
        line += str(chr(65 + row) + str(col))
    print(line)
