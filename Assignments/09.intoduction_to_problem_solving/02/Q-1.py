# Problem 1: Take two numbers and print their sum.
#
# IPO MODEL
# Input: Two integers, first_number and second_number.
# Processing: Add the two numbers.
# Output: Their sum.
#
# ALGORITHM
# 1. Start.
# 2. Read first_number and second_number.
# 3. Set total to first_number + second_number.
# 4. Print total.
# 5. Stop.
#
# DRY RUNS
# Case 1: first_number=10, second_number=20 -> total=30 -> output 30.
# Case 2: first_number=-4, second_number=4 -> total=0 -> output 0.

first_number = int(input())
second_number = int(input())

total = first_number + second_number
print(total)
