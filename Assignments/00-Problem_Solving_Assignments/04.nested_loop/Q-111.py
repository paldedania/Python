# Q111. Matrix Comparison
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows = int(input())
columns = rows
a = []
b = []
for matrix in (a, b):
    for row in range(rows):
        values = input().split()
        if len(values) != columns:
            raise ValueError("Incorrect row width")
        matrix.append(values)
equal = different = 0
for row in range(rows):
    for col in range(columns):
        same = float(a[row][col]) == float(b[row][col])
        print(row, col, "Equal" if same else "Different")
        if same:
            equal += 1
        else:
            different += 1
print("Equal positions =", equal, "Different positions =", different)
