number = int(input("Number (1-10): "))

while number < 1 or number > 10:
    print("Invalid.")
    number = int(input("Number (1-10): "))

print("Number:", number)
