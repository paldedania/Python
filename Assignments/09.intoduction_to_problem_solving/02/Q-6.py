# Problem 6: Calculate the average of three subject marks and print Pass or Fail.
# A Pass requires an average of at least 40.
#
# IPO MODEL
# Input: Three subject marks.
# Processing: Calculate (mark1 + mark2 + mark3) / 3, then compare it with 40.
# Output: Pass if the average is at least 40; otherwise Fail.
#
# ALGORITHM
# 1. Start.
# 2. Read mark1, mark2, and mark3.
# 3. Calculate average = (mark1 + mark2 + mark3) / 3.
# 4. If average >= 40, print Pass.
# 5. Otherwise, print Fail.
# 6. Stop.
#
# DRY RUNS
# Case 1: marks=50, 40, 30 -> average=40 -> output Pass.
# Case 2: marks=39, 40, 40 -> average=39.67 -> output Fail.

mark1 = float(input())
mark2 = float(input())
mark3 = float(input())

average = (mark1 + mark2 + mark3) / 3

if average >= 40:
    print("Pass")
else:
    print("Fail")
