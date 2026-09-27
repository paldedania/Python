alphabet = "ABCDE"
row = 1
while row <= 5:
    count = 0
    while count < row:
        print(alphabet[row - 1], end=" ")
        count += 1
    print()
    row += 1
