balance = float(input("Enter starting balance: "))

deposit_count = 0
withdrawal_count = 0
rejected_withdrawals = 0

for i in range(7):
    transaction = input("Enter Deposit or Withdrawal: ").lower()
    amount = float(input("Enter amount: "))

    if transaction == "deposit":
        balance += amount
        deposit_count += 1
        print("Deposit successful")

    elif transaction == "withdrawal":
        withdrawal_count += 1

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            rejected_withdrawals += 1
            print("Withdrawal rejected due to insufficient balance")

    else:
        print("Invalid transaction")

    if balance < 1000:
        print("Low Balance")

    print("Current balance:", balance)
    print()

print("Final balance:", balance)
print("Deposits:", deposit_count)
print("Withdrawal attempts:", withdrawal_count)
print("Rejected withdrawals:", rejected_withdrawals)