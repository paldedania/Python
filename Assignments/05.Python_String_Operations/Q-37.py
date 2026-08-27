text = "Python"

try:
    print(text[20])
except IndexError as error:
    print("A Error:", type(error).__name__)
    print("Reason: Index 20 is outside the string.")
    print("Corrected Output:", text[0])

try:
    text[0] = "J"
except TypeError as error:
    print("\nB Error:", type(error).__name__)
    print("Reason: Strings cannot be changed character by character.")
    corrected_text = "J" + text[1:]
    print("Corrected Output:", corrected_text)

age = 20

try:
    print("Age: " + age)
except TypeError as error:
    print("\nC Error:", type(error).__name__)
    print("Reason: A string and an integer cannot be joined using +.")
    print("Corrected Output: Age: " + str(age))

try:
    print(text.index("Java"))
except ValueError as error:
    print("\nD Error:", type(error).__name__)
    print("Reason: Java does not exist in the string.")
    print("Corrected Output using find():", text.find("Java"))
