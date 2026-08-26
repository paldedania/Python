word = "Python "

print("String repeated three times:", word * 3)

try:
    print(word * 3.0)
except TypeError as error:
    print("String multiplied by a float:", type(error).__name__, "-", error)
