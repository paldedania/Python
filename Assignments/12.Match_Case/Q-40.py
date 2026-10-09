role = int(input("Enter role (1=Student, 2=Teacher, 3=Administration): "))

match role:
    case 1:
        option = int(input("Enter student option (1=Profile, 2=Marks, 3=Attendance, 4=Courses): "))
        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Student Option")
    case 2:
        option = int(input("Enter teacher option (1=Students, 2=Enter Marks, 3=Attendance, 4=Courses): "))
        match option:
            case 1:
                print("Opening Students")
            case 2:
                print("Entering Marks")
            case 3:
                print("Opening Attendance")
            case 4:
                print("Opening Courses")
            case _:
                print("Invalid Teacher Option")
    case 3:
        option = int(input("Enter administration option (1=Fees, 2=Admissions, 3=Notices, 4=Departments): "))
        match option:
            case 1:
                print("Opening Fees")
            case 2:
                print("Opening Admissions")
            case 3:
                print("Opening Notices")
            case 4:
                print("Opening Departments")
            case _:
                print("Invalid Administration Option")
    case _:
        print("Invalid Role")
