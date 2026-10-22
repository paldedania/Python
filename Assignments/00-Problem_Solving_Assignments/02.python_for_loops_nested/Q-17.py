# Outer loop controls rows; inner loop controls items in a row.
for row in range(3):
    line = ""
    for col in range(1, 4):
        if line:
            line += ' '
        line += str(row * 3 + col)
    print(line)
