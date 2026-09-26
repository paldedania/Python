matrix = []
main_sum = 0
secondary_sum = 0
main_even = 0
secondary_odd = 0

for i in range(4):
    row = []
    for j in range(4):
        number = int(input("Enter a matrix value: "))
        row.append(number)
        if i == j:
            main_sum += number
            if number % 2 == 0:
                main_even += 1
        if i + j == 3:
            secondary_sum += number
            if number % 2 != 0:
                secondary_odd += 1
    matrix.append(row)

print("Main diagonal sum:", main_sum)
print("Secondary diagonal sum:", secondary_sum)
print("Even values on main diagonal:", main_even)
print("Odd values on secondary diagonal:", secondary_odd)

if main_sum > secondary_sum:
    print("Main diagonal sum is greater")
elif secondary_sum > main_sum:
    print("Secondary diagonal sum is greater")
else:
    print("Both diagonal sums are equal")
