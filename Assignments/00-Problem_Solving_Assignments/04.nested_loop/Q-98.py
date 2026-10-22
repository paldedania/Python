# Q98. Shopping Cart Price Matrix
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
customers = int(input())
products = int(input())
prices = input().split()
if len(prices) != products:
    raise ValueError("Enter one price per product")
product_totals = [0] * products
for customer in range(customers):
    quantities = input().split()
    if len(quantities) != products:
        raise ValueError("Enter one quantity per product")
    bill = 0
    for product in range(products):
        quantity = int(quantities[product])
        bill += quantity * float(prices[product])
        product_totals[product] += quantity
    print("Customer", customer + 1, "Total =", bill)
for product in range(products):
    print("Product", product + 1, "Quantity =", product_totals[product])
