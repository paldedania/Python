items = input("Enter integers separated by spaces: ").split()

for item in items:
    number = int(item)
    if number < 0:
        continue
    if number % 4 == 0 and number % 6 == 0:
        print("Found:", number)
        break
else:
    print("No matching number")
