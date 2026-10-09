choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

match choice:
    case 1:
        print(f"{value * 1000:g} meters")
    case 2:
        print(f"{value / 1000:g} kilometers")
    case 3:
        print(f"{value * 1000:g} grams")
    case 4:
        print(f"{value / 1000:g} kilograms")
    case _:
        print("Invalid Choice")
