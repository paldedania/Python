choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Starting Game")
    case 2:
        print("Loading Game")
    case 3:
        setting = int(input("Settings: 1=Sound, 2=Graphics, 3=Controls: "))
        match setting:
            case 1:
                print("Sound Settings Opened")
            case 2:
                print("Graphics Settings Opened")
            case 3:
                print("Controls Settings Opened")
            case _:
                print("Invalid Setting")
    case 4:
        print("Exiting")
    case _:
        print("Invalid Choice")
