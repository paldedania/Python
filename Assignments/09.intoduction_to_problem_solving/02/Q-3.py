# Problem 3: Take three numbers and print the largest number.
#
# IPO MODEL
# Input: Three integers, first_number, second_number, and third_number.
# Processing: Compare the three values to find the largest.
# Output: The largest number.
#
# ALGORITHM
# 1. Start.
# 2. Read the three numbers.
# 3. If first_number is at least as large as both others, select it.
# 4. Otherwise, if second_number is at least as large as both others, select it.
# 5. Otherwise, select third_number.
# 6. Print the selected value.
# 7. Stop.
#
# DRY RUNS
# Case 1: 3, 9, 5 -> 9 is largest -> output 9.
# Case 2: -2, -8, -1 -> -1 is largest -> output -1.

first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number >= second_number and first_number >= third_number:
    largest = first_number
elif second_number >= first_number and second_number >= third_number:
    largest = second_number
else:
    largest = third_number

print(largest)
