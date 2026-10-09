choice = int(input("Enter choice: "))
temperature = float(input("Enter temperature: "))

match choice:
    case 1:
        converted = (temperature * 9 / 5) + 32
        print(f"Temperature = {converted} F")
    case 2:
        converted = (temperature - 32) * 5 / 9
        print(f"Temperature = {converted} C")
    case _:
        print("Invalid Choice")
