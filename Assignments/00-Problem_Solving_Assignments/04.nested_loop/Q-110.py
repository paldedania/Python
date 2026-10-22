# Q110. Matrix Border and Diagonal Analyzer
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows = int(input())
columns = int(input())
matrix = []
for row in range(rows):
    values = input().split()
    if len(values) != columns:
        raise ValueError("Incorrect row width")
    matrix.append(values)
total = border = main = opposite = inner = 0
for row in range(rows):
    for col in range(columns):
        value = float(matrix[row][col])
        total += value
        if row == 0 or row == rows - 1 or col == 0 or col == columns - 1:
            border += value
        else:
            inner += value
        if row == col:
            main += value
        if row + col == columns - 1:
            opposite += value
print("Total =", total, "Border =", border, "Main diagonal =", main, "Opposite diagonal =", opposite, "Inner =", inner)
