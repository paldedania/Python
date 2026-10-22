# Outer loop controls rows; inner loop controls items in a row.
for row in range(5, 0, -1):
    line = ""
    for col in range(row):
        if line:
            line += ' '
        line += str("*")
    print(line)
