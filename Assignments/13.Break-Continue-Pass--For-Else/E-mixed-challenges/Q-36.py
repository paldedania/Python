items = input("Enter integers separated by spaces: ").split()
target = int(input("Enter the target number: "))

for item in items:
    number = int(item)
    if number < 0:
        continue
    if number == target:
        print("Target found")
        break
else:
    print("Target not found")
