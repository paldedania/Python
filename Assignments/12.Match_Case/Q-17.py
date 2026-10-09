account_type = int(input("Enter account type: "))

match account_type:
    case 1:
        account_name = "Savings"
    case 2:
        account_name = "Current"
    case _:
        account_name = None
        print("Invalid Account Type")

if account_name is not None:
    operation = int(input("Enter operation: "))
    print(f"{account_name} Account")
    match operation:
        case 1:
            print("Check Balance Selected")
        case 2:
            print("Deposit Selected")
        case 3:
            print("Withdraw Selected")
        case _:
            print("Invalid Operation")
