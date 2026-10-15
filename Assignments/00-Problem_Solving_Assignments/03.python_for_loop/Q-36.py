total_revenue = 0

for customer in range(5):
    subtotal = 0
    for item in range(3):
        price = float(input("Enter item price: "))
        subtotal += price

    member = input("Is the customer a member? (yes/no): ").lower()
    if subtotal >= 2000:
        discount = 15
    elif subtotal >= 1000:
        discount = 10
    else:
        discount = 0

    final_bill = subtotal - (subtotal * discount / 100)
    if member == "yes":
        final_bill = final_bill - (final_bill * 5 / 100)

    total_revenue += final_bill
    print("Subtotal:", subtotal)
    print("Final bill:", final_bill)

print("Total restaurant revenue:", total_revenue)
