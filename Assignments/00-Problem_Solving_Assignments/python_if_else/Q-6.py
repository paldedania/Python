number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print("Divisible by both 5 and 11")
elif number % 5 == 0:
    print("Divisible only by 5")
elif number % 11 == 0:
    print("Divisible only by 11")
else:
    print("Divisible by neither")
