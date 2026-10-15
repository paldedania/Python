number = int(input("Number (1-100): "))

while number < 1 or number > 100:
    print("Invalid.")
    number = int(input("Number (1-100): "))

print("Number:", number)
