# 24. Define apply_discount(price, discount=0) that returns the final price after subtracting the discount percentage. Assume discount is between 0 and 100.

def apply_discount(price, discount=0):
    return price - price * discount / 100


print(apply_discount(1000))
print(apply_discount(1000, discount=20))
