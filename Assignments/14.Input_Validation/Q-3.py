age = int(input("Age (0-120): "))

while age < 0 or age > 120:
    print("Invalid.")
    age = int(input("Age (0-120): "))

print("Age:", age)
