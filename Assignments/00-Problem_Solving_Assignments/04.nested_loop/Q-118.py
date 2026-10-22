# Q118. Cricket Score Matrix
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows = int(input())
columns = int(input())
matrix = []
for row in range(rows):
    values = input().split()
    if len(values) != columns:
        raise ValueError("Incorrect row width")
    matrix.append(values)
column_totals = [0] * columns
highest_total = None
best_row = 0
for row in range(rows):
    total = 0
    for col in range(columns):
        value = float(matrix[row][col])
        total += value
        column_totals[col] += value
    print("Player", row + 1, "Total =", total)
    if highest_total is None or total > highest_total:
        highest_total = total
        best_row = row + 1
if rows:
    print("Highest total: Player", best_row, "=", highest_total)
best_column = 0
highest_column = None
for col in range(columns):
    print("Match", col + 1, "Total =", column_totals[col])
    if highest_column is None or column_totals[col] > highest_column:
        highest_column = column_totals[col]
        best_column = col + 1
if columns:
    print("Highest total: Match", best_column, "=", highest_column)
