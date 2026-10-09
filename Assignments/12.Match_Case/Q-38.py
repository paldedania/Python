choice = int(input("Enter dashboard option (1=Engine, 2=Lights, 3=Music, 4=Navigation): "))

match choice:
    case 1:
        action = int(input("Engine (1=Start, 2=Stop): "))
        match action:
            case 1:
                print("Engine Start Selected")
            case 2:
                print("Engine Stop Selected")
            case _:
                print("Invalid Engine Option")
    case 2:
        action = int(input("Lights (1=Headlights, 2=Indicators, 3=Hazard Lights): "))
        match action:
            case 1:
                print("Headlights Selected")
            case 2:
                print("Indicators Selected")
            case 3:
                print("Hazard Lights Selected")
            case _:
                print("Invalid Lights Option")
    case 3:
        action = int(input("Music (1=Play, 2=Pause, 3=Next, 4=Previous): "))
        match action:
            case 1:
                print("Play Selected")
            case 2:
                print("Pause Selected")
            case 3:
                print("Next Selected")
            case 4:
                print("Previous Selected")
            case _:
                print("Invalid Music Option")
    case 4:
        action = int(input("Navigation (1=Start, 2=Stop): "))
        match action:
            case 1:
                print("Start Navigation Selected")
            case 2:
                print("Stop Navigation Selected")
            case _:
                print("Invalid Navigation Option")
    case _:
        print("Invalid Dashboard Option")
