user_type = int(input("Enter user type: "))

match user_type:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Marks")
            case 2:
                print("Opening Student Attendance")
            case 3:
                print("Opening Student Homework")
            case _:
                print("Invalid Student Option")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Entering Marks")
            case 2:
                print("Taking Attendance")
            case 3:
                print("Assigning Homework")
            case _:
                print("Invalid Teacher Option")
    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Child Marks")
            case 2:
                print("Opening Child Attendance")
            case 3:
                print("Opening Contact Teacher")
            case _:
                print("Invalid Parent Option")
    case _:
        print("Invalid User Type")
