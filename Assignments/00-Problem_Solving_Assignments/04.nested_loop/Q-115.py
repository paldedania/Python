# Q115. Word Search Grid
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows = int(input())
columns = int(input())
matrix = []
for row in range(rows):
    values = input().split()
    if len(values) != columns:
        raise ValueError("Incorrect row width")
    matrix.append(values)
target = input()
found = False
for row in range(rows):
    for col in range(columns):
        if matrix[row][col] == target:
            print(row, col)
            found = True
if not found:
    print("Not found")
