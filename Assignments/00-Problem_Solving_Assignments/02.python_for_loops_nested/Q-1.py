# Outer loop controls rows; inner loop controls items in a row.
for row in range(3):
    line = ""
    for col in range(3):
        if line:
            line += ' '
        line += str("*")
    print(line)
