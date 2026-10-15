balance = 10000
choice = 0

while choice != 4:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    choice = int(input("Choice: "))

    if choice < 1 or choice > 4:
        print("Invalid.")
    elif choice == 1:
        print("Current balance: ₹", balance)
    elif choice == 2:
        deposit = float(input("Deposit: "))
        while deposit <= 0:
            print("Invalid.")
            deposit = float(input("Deposit: "))
        balance = balance + deposit
        print("Balance: ₹", balance)
    elif choice == 3:
        withdrawal = float(input("Withdraw: "))
        while withdrawal <= 0 or withdrawal > balance:
            print("Invalid.")
            withdrawal = float(input("Withdraw: "))
        balance = balance - withdrawal
        print("Balance: ₹", balance)

