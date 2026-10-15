items = input("Enter integers separated by spaces: ").split()

for item in items:
    number = int(item)
    if number == 0:
        continue
    if number == -1:
        break
    print(number, end=" ")
else:
    print()
    print("All values processed")
print()
