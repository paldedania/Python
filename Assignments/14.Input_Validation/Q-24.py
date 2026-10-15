balance = 10000
amount = float(input("Amount (₹100s): "))

while amount <= 0 or amount > balance or amount % 100 != 0:
    print("Invalid.")
    amount = float(input("Amount (₹100s): "))

balance = balance - amount
print("Withdrawn: ₹", amount)
print("Balance: ₹", balance)
