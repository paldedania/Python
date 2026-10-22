# Outer loop controls rows; inner loop controls items in a row.
for row in range(1, 4):
    line = ""
    for col in range(1, 4):
        if line:
            line += ' '
        line += str("(" + str(row) + "," + str(col) + ")")
    print(line)
