cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if cost_price < 0 or selling_price < 0:
    print("Invalid price")
elif selling_price > cost_price:
    print("Profit =", selling_price - cost_price)
elif cost_price > selling_price:
    print("Loss =", cost_price - selling_price)
else:
    print("No profit and no loss")
