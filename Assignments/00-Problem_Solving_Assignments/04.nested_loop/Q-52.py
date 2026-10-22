# Q52. Prime Factor Display
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
for number in range(2, n + 1):
    prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            prime = False
    if prime:
        print(number, "->", 1, number)
