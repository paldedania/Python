first_number = float(input("First: "))
operator = input("Operator: ")

while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Invalid operator.")
    operator = input("Operator: ")

second_number = float(input("Second: "))
while operator == "/" and second_number == 0:
    print("Cannot divide by zero.")
    second_number = float(input("Second: "))

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
else:
    result = first_number / second_number

print("Result:", result)
