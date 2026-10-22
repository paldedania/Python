# Outer loop controls rows; inner loop controls items in a row.
for row in range(1, 4):
    line = ""
    for col in range(1, 6):
        if line:
            line += ' '
        line += str(row * col)
    print(line)
