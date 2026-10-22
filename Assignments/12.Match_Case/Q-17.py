account_type = int(input("Enter account type: "))

match account_type:
    case 1:
        print("Savings Account")
        operation = int(input("Enter operation: "))
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")
    case 2:
        print("Current Account")
        operation = int(input("Enter operation: "))
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")
    case _:
        print("Invalid Account Type")
