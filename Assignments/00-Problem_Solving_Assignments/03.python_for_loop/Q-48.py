clean = 0
acceptable = 0
invalid = 0

for i in range(10):
    username = input("Enter username: ")
    letters = 0
    digits = 0
    underscores = 0
    has_space = False
    has_other_special = False

    for char in username:
        if ("a" <= char <= "z") or ("A" <= char <= "Z"):
            letters += 1
        elif "0" <= char <= "9":
            digits += 1
        elif char == "_":
            underscores += 1
        elif char == " ":
            has_space = True
        else:
            has_other_special = True

    if has_space or has_other_special or len(username) < 3 or len(username) > 20:
        result = "Invalid"
        invalid += 1
    elif len(username) >= 5 and has_space == False and has_other_special == False:
        result = "Clean"
        clean += 1
    else:
        result = "Acceptable"
        acceptable += 1

    print("Letters:", letters)
    print("Digits:", digits)
    print("Underscores:", underscores)
    print(result)

print("Clean:", clean)
print("Acceptable:", acceptable)
print("Invalid:", invalid)
