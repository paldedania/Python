
n = int(input("Enter n: "))

for number in range(1, n + 1):
    if number % 3 == 0:
        continue
    print(number, end=" ")
print()
