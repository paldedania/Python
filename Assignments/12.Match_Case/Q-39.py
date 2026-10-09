user_type = int(input("Enter user type (1=Employee, 2=Manager): "))

match user_type:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Employee Profile")
            case 2:
                leave_days = int(input("Enter number of leave days: "))
                if leave_days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")
            case 3:
                print("Opening Employee Salary")
            case _:
                print("Invalid Employee Option")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Team")
            case 2:
                print("Approving Leave")
            case 3:
                print("Opening Reports")
            case _:
                print("Invalid Manager Option")
    case _:
        print("Invalid User Type")
