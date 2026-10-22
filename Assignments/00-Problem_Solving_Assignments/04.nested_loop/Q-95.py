# Q95. Prime Pair Generator
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
for a in range(2, n + 1):
    prime_a = True
    for divisor in range(2, a):
        if a % divisor == 0:
            prime_a = False
    if prime_a:
        for b in range(a, n + 1):
            prime_b = True
            prime_sum = True
            for divisor in range(2, b):
                if b % divisor == 0:
                    prime_b = False
            for divisor in range(2, a + b):
                if (a + b) % divisor == 0:
                    prime_sum = False
            if prime_b and prime_sum:
                print(a, "+", b, "=", a + b)
