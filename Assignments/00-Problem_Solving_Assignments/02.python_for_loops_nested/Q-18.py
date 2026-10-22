# Outer loop controls rows; inner loop controls items in a row.
for row in range(4):
    line = ""
    for col in range(1, 6):
        if line:
            line += ' '
        line += str(row * 5 + col)
    print(line)
