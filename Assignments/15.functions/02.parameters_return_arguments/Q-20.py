# 20. Define bill(item, quantity=1, price=100) that returns the bill amount. Test positional and keyword calls.

def bill(item, quantity=1, price=100):
    return quantity * price


print(bill("Notebook"))
print(bill("Notebook", 3, 50))
print(bill(item="Notebook", price=50, quantity=2))
print(bill("Notebook", price=50))
