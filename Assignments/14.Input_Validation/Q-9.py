number = int(input("Number: "))

while number <= 0 or number % 3 != 0 or number % 5 != 0:
    print("Invalid.")
    number = int(input("Number: "))

print("Number:", number)
