value = None
number = 5

try:
    print("Addition:", value + number)
except TypeError as error:
    print("Addition:", type(error).__name__, "-", error)

try:
    print("Subtraction:", value - number)
except TypeError as error:
    print("Subtraction:", type(error).__name__, "-", error)

try:
    print("Multiplication:", value * number)
except TypeError as error:
    print("Multiplication:", type(error).__name__, "-", error)

try:
    print("Division:", value / number)
except TypeError as error:
    print("Division:", type(error).__name__, "-", error)

try:
    print("Floor Division:", value // number)
except TypeError as error:
    print("Floor Division:", type(error).__name__, "-", error)

try:
    print("Modulus:", value % number)
except TypeError as error:
    print("Modulus:", type(error).__name__, "-", error)

try:
    print("Exponentiation:", value ** number)
except TypeError as error:
    print("Exponentiation:", type(error).__name__, "-", error)

print("\nNone represents the absence of a value, not a number.")
print("Therefore, Python cannot use None directly in arithmetic operations.")
