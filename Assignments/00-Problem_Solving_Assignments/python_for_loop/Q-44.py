balance = float(input("Enter starting balance: "))
transactions = int(input("How many transactions? "))
total_deposits = 0
total_withdrawals = 0

for i in range(transactions):
    transaction = input("Enter D for deposit or W for withdrawal: ").upper()
    amount = float(input("Enter amount: "))

    if transaction == "D":
        balance += amount
        total_deposits += amount
    elif transaction == "W":
        balance -= amount
        total_withdrawals += amount
    else:
        print("Invalid transaction")

if balance < 0:
        print("Overdraft")
elif balance < 500:
    print("Low Balance")
else:
    print("Normal")

print("Total deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Final balance:", balance)
