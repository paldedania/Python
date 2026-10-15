while True:
    print("1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")
    choice = int(input("Choice: "))
    if choice >= 1 and choice <= 4:
        break
    print("Invalid.\n")

print("Choice:", choice)
