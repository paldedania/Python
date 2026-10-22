# 11. Define calculate(a, b) that returns the sum, difference, product, and quotient. Assume b is not zero.

def calculate(a, b):
    # The exercise assumes b is not zero.
    return a + b, a - b, a * b, a / b


total, difference, product, quotient = calculate(10, 4)
print("Sum:", total)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
