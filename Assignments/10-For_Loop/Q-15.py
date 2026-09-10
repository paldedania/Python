num = int(input("Enter a positive number: "))
count = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        count = count + 1

print(count)
