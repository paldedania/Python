# 4. Given values = [4, 5, 6], call a three-parameter function by unpacking values.

def add_three(a, b, c):
    return a + b + c


values = [4, 5, 6]
print(add_three(*values))  # Equivalent to add_three(4, 5, 6).
