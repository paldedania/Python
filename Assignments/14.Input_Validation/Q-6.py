temperature = float(input("Temp (-20 to 45): "))

while temperature < -20 or temperature > 45:
    print("Invalid.")
    temperature = float(input("Temp (-20 to 45): "))

print("Temp:", temperature)
