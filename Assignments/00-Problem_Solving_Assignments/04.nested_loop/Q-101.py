# Q101. Pattern + Condition Challenge
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
# Main diagonal A takes priority at the center.
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(n):
    line = ""
    for col in range(n):
        if line:
            line += ' '
        line += str("A" if row == col else "B" if row + col == n - 1 else "-")
    print(line)
