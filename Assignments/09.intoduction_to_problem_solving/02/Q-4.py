# Problem 4: Check whether a person is eligible to vote (minimum age 18).
#
# IPO MODEL
# Input: The person's age as an integer.
# Processing: Check whether age is at least 18.
# Output: Eligible to vote or Not eligible to vote.
#
# ALGORITHM
# 1. Start.
# 2. Read age.
# 3. If age >= 18, print Eligible to vote.
# 4. Otherwise, print Not eligible to vote.
# 5. Stop.
#
# DRY RUNS
# Case 1: age=18 -> 18 >= 18 is true -> output Eligible to vote.
# Case 2: age=17 -> 17 >= 18 is false -> output Not eligible to vote.

age = int(input())

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
