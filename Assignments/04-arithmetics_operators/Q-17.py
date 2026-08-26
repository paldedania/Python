first_string = "Hello"
second_string = "Python"

print("string + string:", first_string + second_string)

try:
    print("string - string:", first_string - second_string)
except TypeError as error:
    print("string - string:", type(error).__name__, "-", error)

print("string * integer:", first_string * 3)

try:
    print("string / string:", first_string / second_string)
except TypeError as error:
    print("string / string:", type(error).__name__, "-", error)

print("\nConcatenation and repetition work.")
print("Subtraction and division are not supported for strings.")
