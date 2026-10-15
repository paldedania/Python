code = input("Enter the product code: ")
valid = len(code) == 8

if valid:
    for i in range(3):
        if not ("A" <= code[i] <= "Z"):
            valid = False

    for i in range(3, 8):
        if not ("0" <= code[i] <= "9"):
            valid = False

if valid:
    print("Valid Product Code")
else:
    print("Invalid Product Code")
