# Q74. Multiplication Table Matrix
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
for number in range(1, n + 1):
    for multiplier in range(1, 11):
        print(number, "x", multiplier, "=", number * multiplier)
