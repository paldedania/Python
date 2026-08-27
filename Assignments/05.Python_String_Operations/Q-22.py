text = "Python is a programming language"

print("Position of Python:", text.index("Python"))
print("Position of programming:", text.index("programming"))
print("Position of language:", text.index("language"))

try:
    print("Position of Java:", text.index("Java"))
except ValueError as error:
    print("Error:", type(error).__name__)
    print("index() raises an error when the text does not exist.")
