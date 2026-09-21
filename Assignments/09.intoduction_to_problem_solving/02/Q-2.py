# Problem 2: Take a number and print whether it is even or odd.
#
# IPO MODEL
# Input: One integer, number.
# Processing: Check the remainder when number is divided by 2.
# Output: Even when the remainder is 0; otherwise Odd.
#
# ALGORITHM
# 1. Start.
# 2. Read number.
# 3. If number % 2 equals 0, print Even.
# 4. Otherwise, print Odd.
# 5. Stop.
#
# DRY RUNS
# Case 1: number=8 -> 8 % 2=0 -> output Even.
# Case 2: number=7 -> 7 % 2=1 -> output Odd.

number = int(input())

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
