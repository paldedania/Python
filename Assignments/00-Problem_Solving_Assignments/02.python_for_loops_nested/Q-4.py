# Outer loop controls rows; inner loop controls items in a row.
for row in range(1, 6):
    line = ""
    for col in range(row):
        if line:
            line += ' '
        line += str("*")
    print(line)
