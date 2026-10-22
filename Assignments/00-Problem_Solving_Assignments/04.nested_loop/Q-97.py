# Q97. Cinema Seat Booking
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows = int(input())
columns = int(input())
matrix = []
for row in range(rows):
    values = input().split()
    if len(values) != columns:
        raise ValueError("Incorrect row width")
    matrix.append(values)
available = 0
occupied = 0
best_row = 0
best_available = -1
fully_booked = 0
for row in range(rows):
    row_available = 0
    for col in range(columns):
        if matrix[row][col] == 'O':
            available += 1
            row_available += 1
        else:
            occupied += 1
    print("Row", row + 1, "Open =", row_available)
    if row_available > best_available:
        best_available = row_available
        best_row = row + 1
    if row_available == 0:
        fully_booked += 1
print("Open =", available, "Booked =", occupied)
if rows > 0:
    print("Most open seats: Row", best_row)
