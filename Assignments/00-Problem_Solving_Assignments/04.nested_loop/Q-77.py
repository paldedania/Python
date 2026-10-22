# Q77. Ticket Price Grid
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows = int(input())
seats = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(rows):
    line = ""
    for col in range(1, seats + 1):
        if line:
            line += ' '
        line += str(100 if col % 2 else 150)
    print(line)
