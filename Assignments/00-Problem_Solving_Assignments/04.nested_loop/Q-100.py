# Q100. Bus Seat Reservation
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
rows = int(input())
columns = 2
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
        if matrix[row][col] == '0':
            available += 1
            row_available += 1
        else:
            occupied += 1
    print("Row", row + 1, "Available =", row_available)
    if row_available > best_available:
        best_available = row_available
        best_row = row + 1
    if row_available == 0:
        fully_booked += 1
print("Available =", available, "Booked =", occupied)
print("Fully booked rows =", fully_booked)
