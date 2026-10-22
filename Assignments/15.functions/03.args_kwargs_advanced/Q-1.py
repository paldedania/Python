# 1. Write multiply_all(*args) that returns the product of all supplied numbers. Decide what it should return when no numbers are supplied.

def multiply_all(*args):
    # With no arguments, return 1, the multiplicative identity.
    product = 1
    for number in args:
        product *= number
    return product


print(multiply_all(2, 3, 4))
print(multiply_all())
print(multiply_all(5, 0, 2))
