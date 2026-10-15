balance = 2000
deposit = float(input("Deposit: "))

while deposit <= 0:
    print("Invalid.")
    deposit = float(input("Deposit: "))

balance = balance + deposit
print("Balance: ₹", balance)
