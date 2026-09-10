num = int(input("Enter a positive number: "))

for row in range(1, num + 1):
    for number in range(1, row + 1):
        print(number, end="")
    print()
