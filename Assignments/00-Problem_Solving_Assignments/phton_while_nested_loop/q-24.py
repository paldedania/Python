row = 5
while row >= 1:
    number = 5
    while number >= 6 - row:
        print(number, end="")
        number -= 1
    print()
    row -= 1
