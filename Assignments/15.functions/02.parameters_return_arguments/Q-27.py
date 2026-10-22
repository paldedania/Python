# 27. Define compare(a, b) that returns two values: "A is greater", "B is greater", or "Equal" as the first value, and the absolute difference as the second value. Do not use abs().

def compare(a, b):
    if a > b:
        return "A is greater", a - b
    if b > a:
        return "B is greater", b - a
    return "Equal", 0


print(compare(10, 4))
print(compare(4, 10))
print(compare(5, 5))
