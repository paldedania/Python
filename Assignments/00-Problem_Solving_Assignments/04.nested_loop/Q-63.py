# Q63. Repeated Number Pyramid
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
for row in range(1, n + 1):
    line = ""
    for space in range(n - row):
        line += " "
    for col in range(1, 2 * row - 1 + 1):
        line += str(row)
    print(line)
