# Outer loop controls rows; inner loop controls items in a row.
for row in range(1, 6):
    line = ""
    for col in range(5, row - 1, -1):
        if line:
            line += ''
        line += str(col)
    print(line)
