password = input("Password: ")

while True:
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_whitespace = False

    for character in password:
        if character.isupper():
            has_uppercase = True
        if character.islower():
            has_lowercase = True
        if character.isdigit():
            has_digit = True
        if character.isspace():
            has_whitespace = True

    length_is_valid = len(password) >= 8
    if length_is_valid and has_uppercase and has_lowercase and has_digit and not has_whitespace:
        break

    print("Missing:")
    if not length_is_valid:
        print("- 8+ characters")
    if not has_uppercase:
        print("- uppercase letter")
    if not has_lowercase:
        print("- lowercase letter")
    if not has_digit:
        print("- digit")
    if has_whitespace:
        print("- no spaces")
    password = input("Password: ")

print("OK.")
