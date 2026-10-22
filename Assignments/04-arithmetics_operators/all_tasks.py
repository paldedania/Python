# All practical tasks from 04.Arithmetic_Operators/Assignment.md
# Run with Python 3. Input is requested at the tasks that require it.


# Task 1
a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# Task 2
integer_number = 10
float_number = 2.5

result = integer_number + float_number
print("Addition:", result, "-", type(result))

result = integer_number - float_number
print("Subtraction:", result, "-", type(result))

result = integer_number * float_number
print("Multiplication:", result, "-", type(result))

result = integer_number / float_number
print("Division:", result, "-", type(result))

result = integer_number // float_number
print("Floor Division:", result, "-", type(result))

result = integer_number % float_number
print("Modulus:", result, "-", type(result))

result = integer_number ** float_number
print("Exponentiation:", result, "-", type(result))


# Task 3
maths = 85
science = 90
english = 80

total_marks = maths + science + english
average_marks = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)


# Task 4
product_price = 249.50
quantity = 4

total_price = product_price * quantity

print("Total Price:", total_price)


# Task 5
number = 17

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")


# Task 6
# Positive numbers
a = 7
b = 2

print("Positive numbers:")
print("7 / 2 =", a / b)
print("7 // 2 =", a // b)

# Negative number test
a = -7
b = 2

print("\nNegative number test:")
print("-7 / 2 =", a / b)
print("-7 // 2 =", a // b)


# Task 7
a = -20
b = -6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)


# Task 8
print("10 - 4 =", 10 - 4)
print("10 - (-4) =", 10 - (-4))
print("-10 - 4 =", -10 - 4)
print("-10 - (-4) =", -10 - (-4))


# Task 9
print("7 // 2 =", 7 // 2)
print("-7 // 2 =", -7 // 2)
print("7 // -2 =", 7 // -2)
print("-7 // -2 =", -7 // -2)

print("\nExplanation:")
print("Floor division rounds down toward negative infinity.")
print("Therefore, -3.5 becomes -4, not -3.")
print("Simply removing the decimal part would round it toward zero.")


# Task 10
print("7 % 3 =", 7 % 3)
print("-7 % 3 =", -7 % 3)
print("7 % -3 =", 7 % -3)
print("-7 % -3 =", -7 % -3)

print("\nThe remainder has the same sign as the divisor in Python.")


# Task 11
print("Expression: 10 + 5 * 2")
print("Expected result: 20")
print("Python result:", 10 + 5 * 2)
print("Multiplication is evaluated first.\n")

print("Expression: 20 - 4 / 2")
print("Expected result: 18.0")
print("Python result:", 20 - 4 / 2)
print("Division is evaluated first.\n")

print("Expression: 10 + 20 / 5 * 2")
print("Expected result: 18.0")
print("Python result:", 10 + 20 / 5 * 2)
print("Division and multiplication are evaluated left to right, then addition.\n")

print("Expression: 2 + 3 * 4 ** 2")
print("Expected result: 50")
print("Python result:", 2 + 3 * 4 ** 2)
print("Exponentiation is first, multiplication is second, and addition is last.\n")

print("Expression: 100 - 20 // 5")
print("Expected result: 96")
print("Python result:", 100 - 20 // 5)
print("Floor division is evaluated first.")


# Task 12
print("10 + 5 * 2 =", 10 + 5 * 2)
print("(10 + 5) * 2 =", (10 + 5) * 2)

print("\n20 - 10 / 2 =", 20 - 10 / 2)
print("(20 - 10) / 2 =", (20 - 10) / 2)

print("\n2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

print("\nParentheses change the result because Python evaluates")
print("the expression inside parentheses before other operations.")


# Task 13
result = True + False
print("True + False =", result, "-", type(result))

result = True - False
print("True - False =", result, "-", type(result))

result = True * False
print("True * False =", result, "-", type(result))

result = False / True
print("False / True =", result, "-", type(result))

result = False // True
print("False // True =", result, "-", type(result))

result = False % True
print("False % True =", result, "-", type(result))

result = True ** False
print("True ** False =", result, "-", type(result))


# Task 14
print("True + 5 =", True + 5)
print("False + 5 =", False + 5)
print("True * 10 =", True * 10)
print("False * 10 =", False * 10)
print("True - 5 =", True - 5)
print("False - 5 =", False - 5)

print("\nPython treats True as 1 and False as 0 in arithmetic.")


# Task 15
first_name = "Pal"
last_name = "Patel"

complete_name = first_name + " " + last_name

print("Complete Name:", complete_name)


# Task 16
word = "Python "

print("String repeated three times:", word * 3)

try:
    print(word * 3.0)
except TypeError as error:
    print("String multiplied by a float:", type(error).__name__, "-", error)


# Task 17
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


# Task 18
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


# Task 19
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


# Task 20
first_number = 20
second_number = 6

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)
print("Floor Division:", first_number // second_number)
print("Modulus:", first_number % second_number)
print("Exponentiation:", first_number ** second_number)


# Task 21
a = 10
b = -3
c = 2.5

print("Expression: a + b")
print("Predicted result: 7")
print("Python result:", a + b)
print("Comparison: Prediction is correct.\n")

print("Expression: a - b")
print("Predicted result: 13")
print("Python result:", a - b)
print("Comparison: Prediction is correct.\n")

print("Expression: b * c")
print("Predicted result: -7.5")
print("Python result:", b * c)
print("Comparison: Prediction is correct.\n")

print("Expression: a / c")
print("Predicted result: 4.0")
print("Python result:", a / c)
print("Comparison: Prediction is correct.\n")

print("Expression: a // b")
print("Predicted result: -4")
print("Python result:", a // b)
print("Comparison: Prediction is correct.\n")

print("Expression: a % b")
print("Predicted result: -2")
print("Python result:", a % b)
print("Comparison: Prediction is correct.\n")

print("Expression: a ** 2")
print("Predicted result: 100")
print("Python result:", a ** 2)
print("Comparison: Prediction is correct.\n")

print("Expression: (a + b) * c")
print("Predicted result: 17.5")
print("Python result:", (a + b) * c)
print("Comparison: Prediction is correct.\n")

print("Expression: a + b * c")
print("Predicted result: 2.5")
print("Python result:", a + b * c)
print("Comparison: Prediction is correct.\n")

print("Expression: a - c ** 2")
print("Predicted result: 3.75")
print("Python result:", a - c ** 2)
print("Comparison: Prediction is correct.\n")

print("Expression: (a / c) + b * 2")
print("Predicted result: -2.0")
print("Python result:", (a / c) + b * 2)
print("Comparison: Prediction is correct.\n")

print("Expression: -b + a // 4")
print("Predicted result: 5")
print("Python result:", -b + a // 4)
print("Comparison: Prediction is correct.")
