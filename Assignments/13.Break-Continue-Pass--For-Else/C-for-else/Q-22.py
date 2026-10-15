items = input("Enter integers separated by spaces: ").split()
target = int(input("Enter the target number: "))

for item in items:
    number = int(item)
    if number == target:
        print("Found")
        break
else:
    print("Not found")
