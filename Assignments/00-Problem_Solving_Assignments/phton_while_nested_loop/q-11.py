alphabet = "ABCDE"
row = 1
while row <= 5:
    index = 0
    while index < row:
        print(alphabet[index], end=" ")
        index += 1
    print()
    row += 1
