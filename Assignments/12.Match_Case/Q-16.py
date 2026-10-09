user_type = int(input("Enter user type: "))

match user_type:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Courses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case _:
                print("Invalid Student Option")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Students")
            case 2:
                print("Entering Marks")
            case 3:
                print("Opening Attendance")
            case _:
                print("Invalid Teacher Option")
    case _:
        print("Invalid User Type")
