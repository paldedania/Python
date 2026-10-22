# Q94. Armstrong Numbers in a Range
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
# General Armstrong definition: sum of digits raised to digit count.
for number in range(1, n + 1):
    digits = str(number)
    total = 0
    for digit in digits:
        total += int(digit) ** len(digits)
    if total == number:
        print(number)
