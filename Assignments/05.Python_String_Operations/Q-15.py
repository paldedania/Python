age = 18

try:
    print("Age: " + age)
except TypeError as error:
    print("Error:", type(error).__name__)
    print("Reason: A string and an integer cannot be joined using +.")

print("Corrected Output: Age: " + str(age))
