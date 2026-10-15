balance = 5000
amount = float(input("Withdraw: "))

while amount <= 0 or amount > balance:
    print("Invalid.")
    amount = float(input("Withdraw: "))

balance = balance - amount
print("Balance: ₹", balance)
