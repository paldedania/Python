n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(" " * (2 * (n - i)), end="")

    for j in range(1, i + 1):
        number = j

        if number % 3 == 0 and number % 5 == 0:
            classification = "F"
        elif number % 3 == 0:
            classification = "T"
        elif number % 2 == 0:
            classification = "E"
        else:
            classification = "O"

        print(number, classification, end="   ")

    print()