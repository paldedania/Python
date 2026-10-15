quantity = int(input("Quantity: "))
while quantity <= 0:
    print("Invalid.")
    quantity = int(input("Quantity: "))

unit_price = float(input("Price: "))
while unit_price <= 0:
    print("Invalid.")
    unit_price = float(input("Price: "))

total_cost = quantity * unit_price
print("Total: ₹", total_cost)
