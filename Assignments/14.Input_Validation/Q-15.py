valid_details = False

while not valid_details:
    username = input("Username: ").strip()
    password = input("Password: ")

    username_is_valid = len(username) >= 5 and " " not in username
    password_is_valid = len(password) >= 8 and password.strip() != ""

    if username_is_valid and password_is_valid:
        valid_details = True
    else:
        print("Invalid.")

print("OK.")
