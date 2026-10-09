account_type = int(input("Enter account type: "))

match account_type:
    case 1:
        account = "Savings"
    case 2:
        account = "Current"
    case _:
        account = None
        print("Invalid Account Type")

if account is not None:
    amount = float(input("Enter amount: "))
    print(f"{account} Account")
    if amount > 0:
        print("Withdrawal Request Accepted")
    else:
        print("Invalid Amount")
