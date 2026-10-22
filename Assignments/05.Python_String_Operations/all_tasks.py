# All practical tasks from 05.Python_String_Operations/Assignment.md
# Run with Python 3. Input is requested at the tasks that require it.


# Task 1
name = 'Pal'
city = "Ahmedabad"
favorite_language = 'Python'
message = "I enjoy learning programming."

print("Name:", name)
print("City:", city)
print("Favorite Programming Language:", favorite_language)
print("Message:", message)


# Task 2
text = ""

print("String:", text)
print("Length:", len(text))
print("Data Type:", type(text))


# Task 3
text = "Python Programming"

print("Complete String:", text)
print("Length:", len(text))
print("First Character:", text[0])
print("Last Character:", text[-1])
print("Third Character:", text[2])
print("Second-last Character:", text[-2])


# Task 4
text = "Programming"

print("First Character:", text[0])
print("Second Character:", text[1])
print("Fifth Character:", text[4])
print("Last Character:", text[len(text) - 1])


# Task 5
text = "Programming"

print("Last Character:", text[-1])
print("Second-last Character:", text[-2])
print("Third-last Character:", text[-3])
print("First Character:", text[-len(text)])


# Task 6
full_name = "Pal Patel"

print("First Character:", full_name[0])
print("Last Character:", full_name[-1])
print("First Character of Last Name:", full_name[4])


# Task 7
text = "Python Programming"

print("Python:", text[0:6])
print("Programming:", text[7:18])
print("Complete String:", text[:])
print("First 5 Characters:", text[:5])
print("Last 5 Characters:", text[-5:])


# Task 8
text = "ABCDEFGHIJKL"

print("Every Second Character:", text[::2])
print("Every Third Character:", text[::3])
print("Index 1 to 8 with Step 2:", text[1:9:2])
print("Reversed String:", text[::-1])


# Task 9
text = "Python Programming"

print("Last 5 Characters:", text[-5:])
print("Last 10 Characters:", text[-10:])
print("Characters from End with Negative Step:", text[::-1])


# Task 10
text = "Programming"

print("First 3 Characters:", text[:3])
print("Last 3 Characters:", text[-3:])
print("Every Second Character:", text[::2])
print("Reversed String:", text[::-1])
print("Without First and Last Character:", text[1:-1])


# Task 11
short_word = "Code"
sentence = "Python is easy."
sentence_with_spaces = "I am learning Python."

print("Length of Short Word:", len(short_word))
print("Length of Sentence:", len(sentence))
print("Length of Sentence with Spaces:", len(sentence_with_spaces))
print("Spaces are also counted as characters.")


# Task 12
text = "Python Programming"

last_index = len(text) - 1

print("Last Valid Positive Index:", last_index)
print("Last Character:", text[last_index])


# Task 13
first_name = "Pal"
last_name = "Patel"

full_name = first_name + " " + last_name

print("Full Name:", full_name)


# Task 14
name = "Pal"
age = "18"
city = "Ahmedabad"
programming_language = "Python"

sentence = name + " is " + age + " years old, lives in " + city + ", and learns " + programming_language + "."

print(sentence)


# Task 15
age = 18

try:
    print("Age: " + age)
except TypeError as error:
    print("Error:", type(error).__name__)
    print("Reason: A string and an integer cannot be joined using +.")

print("Corrected Output: Age: " + str(age))


# Task 16
symbol = "#"

print("3 Times:", symbol * 3)
print("5 Times:", symbol * 5)
print("10 Times:", symbol * 10)


# Task 17
symbol = "*"

print(symbol * 10)


# Task 18
text = "python programming language"

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Capitalized:", text.capitalize())
print("Title Case:", text.title())
print("Swap Case:", text.swapcase())


# Task 19
first_text = "Python"
second_text = "python"

print("Direct Comparison:", first_text == second_text)
print("Lowercase Comparison:", first_text.lower() == second_text.lower())


# Task 20
text = "Python is a programming language"

print("Python Exists:", "Python" in text)
print("programming Exists:", "programming" in text)
print("Java Exists:", "Java" in text)
print("language Exists:", "language" in text)


# Task 21
text = "Python is a programming language"

print("Position of Python:", text.find("Python"))
print("Position of programming:", text.find("programming"))
print("Position of language:", text.find("language"))
print("Position of Java:", text.find("Java"))
print("find() returns -1 when the text does not exist.")


# Task 22
text = "Python is a programming language"

print("Position of Python:", text.index("Python"))
print("Position of programming:", text.index("programming"))
print("Position of language:", text.index("language"))

try:
    print("Position of Java:", text.index("Java"))
except ValueError as error:
    print("Error:", type(error).__name__)
    print("index() raises an error when the text does not exist.")


# Task 23
text = "banana"

print("Number of a Characters:", text.count("a"))
print("Number of n Characters:", text.count("n"))
print("Number of b Characters:", text.count("b"))


# Task 24
filename = "student_notes.pdf"

print("Starts with student:", filename.startswith("student"))
print("Ends with .pdf:", filename.endswith(".pdf"))
print("Ends with .txt:", filename.endswith(".txt"))


# Task 25
text = "I am learning Java"

new_text = text.replace("Java", "Python")

print("Original String:", text)
print("New String:", new_text)


# Task 26
text = "apple apple apple"

new_text = text.replace("apple", "mango")

print("Original String:", text)
print("New String:", new_text)


# Task 27
text = "apple apple apple"

new_text = text.replace("apple", "mango", 1)

print("Original String:", text)
print("New String:", new_text)


# Task 28
text = "Python"

text.upper()
print("After Calling upper():", text)

text = text.upper()
print("After Storing the Result:", text)


# Task 29
text = "   Python Programming   "

print("Original:", repr(text))
print("strip():", repr(text.strip()))
print("lstrip():", repr(text.lstrip()))
print("rstrip():", repr(text.rstrip()))


# Task 30
name = input("Enter your name: ")

cleaned_name = name.strip()

print("Cleaned Name:", cleaned_name)


# Task 31
text = "Python is easy to learn"

words = text.split()

print("List of Words:", words)


# Task 32
text = "apple,banana,mango,orange"

fruits = text.split(",")

print("List of Fruits:", fruits)


# Task 33
words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)


# Task 34
words = ["Python", "is", "easy"]

hyphen_text = "-".join(words)
slash_text = "/".join(words)

print(hyphen_text)
print(slash_text)


# Task 35
name = "Pal"
age = 18
city = "Ahmedabad"

sentence = f"My name is {name}, I am {age} years old, and I live in {city}."

print(sentence)


# Task 36
a = 10
b = 20

print(f"The sum is {a + b}")


# Task 37
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


# Task 38
full_name = input("Enter your full name: ")

cleaned_name = full_name.strip()
character = input("Enter a character to search for: ")

print("Original Input:", full_name)
print("Cleaned Name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title Case:", cleaned_name.title())
print("Length:", len(cleaned_name))

if cleaned_name:
    print("First Character:", cleaned_name[0])
    print("Last Character:", cleaned_name[-1])
else:
    print("First Character: The name is empty.")
    print("Last Character: The name is empty.")

print("Contains the Character:", character in cleaned_name)


# Task 39
sentence = input("Enter a sentence: ")
character = input("Enter a character to count: ")

print("Original Sentence:", sentence)
print("Number of Characters:", len(sentence))
print("Number of Words:", len(sentence.split()))

if sentence:
    print("First Character:", sentence[0])
    print("Last Character:", sentence[-1])
else:
    print("First Character: The sentence is empty.")
    print("Last Character: The sentence is empty.")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title Case:", sentence.title())
print("Python Exists:", "Python" in sentence)
print("Chosen Character Count:", sentence.count(character))


# Task 40
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
city = input("Enter your city: ").strip()
course = input("Enter your course: ").strip()
age = input("Enter your age: ").strip()

full_name = first_name + " " + last_name

print("Full Name in Title Case:", full_name.title())
print("Full Name in Uppercase:", full_name.upper())
print("Full Name in Lowercase:", full_name.lower())
print("Length of Full Name:", len(full_name))
print("First Character:", full_name[0])
print("Last Character:", full_name[-1])
print("City:", city)
print("Course:", course)
print(f"Age: {age}")
print("Course Contains Python:", "Python" in course)
print("Course After Replacement:", course.replace("Programming", "Development", 1))
print("Number of Words in Course:", len(course.split()))
