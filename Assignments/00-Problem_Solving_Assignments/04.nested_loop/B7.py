# B7. Prime-Even Pair
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
for a in range(1, n + 1):
    for b in range(1, n + 1):
        prime = True
        for divisor in range(2, a + b):
            if (a + b) % divisor == 0:
                prime = False
        if prime and a * b % 2 == 0:
            print(a, b)
