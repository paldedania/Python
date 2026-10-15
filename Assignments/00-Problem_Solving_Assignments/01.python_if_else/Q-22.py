balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Withdrawal amount must be greater than 0")
elif withdrawal % 100 != 0:
    print("Withdrawal amount must be divisible by 100")
elif withdrawal > balance:
    print("Insufficient balance")
elif balance - withdrawal < 500:
    print("At least 500 must remain in the account")
else:
    remaining_balance = balance - withdrawal
    print("Withdrawal successful")
    print("Remaining balance:", remaining_balance)
