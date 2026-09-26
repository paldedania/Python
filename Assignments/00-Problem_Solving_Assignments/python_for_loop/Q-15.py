even = 0
odd = 0
positive = 0
negative = 0
zero = 0
largest = 0
first_number = True

for i in range(3):
    for j in range(3):
        number = int(input("Enter a matrix value: "))

        if number % 2 == 0:
            even += 1
        else:
            odd += 1

        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        else:
            zero += 1

        if first_number or number > largest:
            largest = number
            first_number = False

print("Even count:", even)
print("Odd count:", odd)
print("Positive count:", positive)
print("Negative count:", negative)
print("Zero count:", zero)
print("Largest number:", largest)
