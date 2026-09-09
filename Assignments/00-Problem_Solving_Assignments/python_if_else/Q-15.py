cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if cost_price <= 0 or selling_price < 0:
    print("Invalid price")
elif selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = profit / cost_price * 100
    print("Profit =", profit)
    print("Profit percentage =", profit_percentage)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percentage = loss / cost_price * 100
    print("Loss =", loss)
    print("Loss percentage =", loss_percentage)
else:
    print("No profit and no loss")
