# Q112. Matrix Addition
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows = int(input())
columns = int(input())
a = []
b = []
for matrix in (a, b):
    for row in range(rows):
        values = input().split()
        if len(values) != columns:
            raise ValueError("Incorrect row width")
        matrix.append(values)
for row in range(rows):
    result = []
    for col in range(columns):
        result.append(str(float(a[row][col]) + float(b[row][col])))
    print(" ".join(result))
