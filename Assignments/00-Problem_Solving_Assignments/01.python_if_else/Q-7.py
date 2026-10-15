number = int(input("Enter a number: "))

if number % 3 == 0 and number % 7 == 0:
    print("Divisible by both 3 and 7")
elif number % 3 == 0:
    print("Divisible only by 3")
elif number % 7 == 0:
    print("Divisible only by 7")
else:
    print("Divisible by neither")
