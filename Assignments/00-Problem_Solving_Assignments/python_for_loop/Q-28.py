numbers = []
even_digit_counts = []

for i in range(10):
    number = int(input("Enter an integer: "))
    number_string = str(number)
    even_count = 0
    odd_count = 0

    for char in number_string:
        if char == "-":
            continue
        if int(char) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    numbers.append(number)
    even_digit_counts.append(even_count)
    print(number, "even digits:", even_count, "odd digits:", odd_count)

highest = 0
for count in even_digit_counts:
    if count > highest:
        highest = count

print("Highest number of even digits:", highest)
print("Numbers with the highest count:")
for i in range(len(numbers)):
    if even_digit_counts[i] == highest:
        print(numbers[i])
