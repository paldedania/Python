count = int(input("Count (1-20): "))
while count < 1 or count > 20:
    print("Invalid.")
    count = int(input("Count (1-20): "))

total = 0
for position in range(1, count + 1):
    value = float(input("Number " + str(position) + ": "))
    total = total + value

average = total / count
print("Average:", average)
