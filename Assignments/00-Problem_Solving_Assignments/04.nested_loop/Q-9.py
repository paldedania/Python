# Q9. Star Rectangle
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows = int(input())
columns = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(rows):
    line = ""
    for col in range(columns):
        if line:
            line += ''
        line += str('*')
    print(line)
