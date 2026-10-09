transport = int(input("Enter transport (1=Flight, 2=Train, 3=Bus): "))

match transport:
    case 1:
        option = int(input("Enter class (1=Economy, 2=Business): "))
        match option:
            case 1:
                print("Flight Economy Selected")
            case 2:
                print("Flight Business Selected")
            case _:
                print("Invalid Flight Class")
    case 2:
        option = int(input("Enter class (1=Sleeper, 2=AC): "))
        match option:
            case 1:
                print("Train Sleeper Selected")
            case 2:
                print("Train AC Selected")
            case _:
                print("Invalid Train Class")
    case 3:
        option = int(input("Enter class (1=Ordinary, 2=Volvo): "))
        match option:
            case 1:
                print("Bus Ordinary Selected")
            case 2:
                print("Bus Volvo Selected")
            case _:
                print("Invalid Bus Class")
    case _:
        print("Invalid Transport")
