# Q113. Matrix Multiplication
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows_a = int(input())
columns_a = int(input())
rows_b = int(input())
columns_b = int(input())
if columns_a != rows_b:
    raise ValueError("Incompatible matrix dimensions")
a = []
b = []
for row in range(rows_a):
    values = input().split()
    if len(values) != columns_a:
        raise ValueError("Incorrect A row width")
    a.append(values)
for row in range(rows_b):
    values = input().split()
    if len(values) != columns_b:
        raise ValueError("Incorrect B row width")
    b.append(values)
for row in range(rows_a):
    line = []
    for col in range(columns_b):
        total = 0
        for k in range(columns_a):
            total += float(a[row][k]) * float(b[k][col])
        line.append(str(total))
    print(" ".join(line))
