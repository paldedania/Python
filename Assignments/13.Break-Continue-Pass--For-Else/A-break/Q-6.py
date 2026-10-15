numbers = input("Enter integers separated by spaces: ").split()

for item in numbers:
    number = int(item)
    if number < 0:
        break
    print(number, end=" ")
print()
