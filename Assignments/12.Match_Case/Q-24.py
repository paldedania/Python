choice = int(input("Enter choice: "))

match choice:
    case 1:
        age = int(input("Enter age: "))
        if age >= 18:
            print("You can start the exam")
        else:
            print("You must be at least 18 to start the exam")
    case 2:
        print("Viewing Result")
    case 3:
        print("Exiting")
    case _:
        print("Invalid Choice")
