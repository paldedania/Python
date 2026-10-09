subject = int(input("Enter subject (1=Programming, 2=Mathematics, 3=Communication): "))

match subject:
    case 1:
        course = int(input("Course (1=Python, 2=Java, 3=C++): "))
        match course:
            case 1:
                print("Python Selected")
            case 2:
                print("Java Selected")
            case 3:
                print("C++ Selected")
            case _:
                print("Invalid Programming Course")
    case 2:
        course = int(input("Course (1=Algebra, 2=Calculus, 3=Statistics): "))
        match course:
            case 1:
                print("Algebra Selected")
            case 2:
                print("Calculus Selected")
            case 3:
                print("Statistics Selected")
            case _:
                print("Invalid Mathematics Course")
    case 3:
        course = int(input("Course (1=English, 2=Presentation, 3=Interview Skills): "))
        match course:
            case 1:
                print("English Selected")
            case 2:
                print("Presentation Selected")
            case 3:
                print("Interview Skills Selected")
            case _:
                print("Invalid Communication Course")
    case _:
        print("Invalid Subject")
