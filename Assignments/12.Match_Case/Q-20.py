first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
operator = input("Enter operator: ").strip()

match operator:
    case "+":
        result = first + second
        print(f"Result = {result:g}")
    case "-":
        result = first - second
        print(f"Result = {result:g}")
    case "*":
        result = first * second
        print(f"Result = {result:g}")
    case "/":
        if second == 0:
            print("Cannot divide by zero")
        else:
            print(f"Result = {first / second:g}")
    case _:
        print("Invalid Operator")
