banking_type = int(input("Enter banking type: "))

match banking_type:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Personal Balance Selected")
            case 2:
                print("Personal Transfer Selected")
            case 3:
                print("Personal Loan Selected")
            case _:
                print("Invalid Personal Banking Option")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Business Balance Selected")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Business Banking Option")
    case _:
        print("Invalid Banking Type")
