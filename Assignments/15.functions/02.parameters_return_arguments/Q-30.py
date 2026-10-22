# 30. Define order_summary(item, quantity=1, price=100, delivery_fee=40) that returns the total cost. Use keyword arguments to change only the delivery fee.

def order_summary(item, quantity=1, price=100, delivery_fee=40):
    return quantity * price + delivery_fee


print(order_summary("Notebook"))
print(order_summary("Notebook", delivery_fee=0))
