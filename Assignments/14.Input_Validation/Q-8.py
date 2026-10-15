username = input("Username: ").strip()

while len(username) < 5 or " " in username:
    print("Invalid.")
    username = input("Username: ").strip()

print("Username:", username)
