# B4. Factor-Sum Challenge
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
for number in range(1, n + 1):
    total = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            total += divisor
    if total == number:
        print(number)
