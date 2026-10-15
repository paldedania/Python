number = int(input("Number (10-50): "))

while number < 10 or number > 50:
    print("Invalid.")
    number = int(input("Number (10-50): "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
