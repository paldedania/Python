print("Division by Zero:")
try:
    print(10 / 0)
except ZeroDivisionError as error:
    print(type(error).__name__, "-", error)

print("\nInvalid String Arithmetic:")
try:
    print("Hello" - "World")
except TypeError as error:
    print(type(error).__name__, "-", error)

print("\nArithmetic with None:")
try:
    print(None + 5)
except TypeError as error:
    print(type(error).__name__, "-", error)
