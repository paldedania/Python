n = int(input("Enter n: "))

for i in range(1, n + 1):
    for number in range(1, i + 1):
        divisor_count = 0
        for divisor in range(1, number + 1):
            if number % divisor == 0:
                divisor_count += 1

        if divisor_count == 2:
            print("P", end=" ")
        elif number % 2 == 0:
            print("E", end=" ")
        else:
            print("O", end=" ")
    print()
