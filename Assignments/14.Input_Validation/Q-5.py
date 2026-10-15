password = input("Password: ")

while len(password.strip()) < 8:
    print("Too short.")
    password = input("Password: ")

print("OK.")
