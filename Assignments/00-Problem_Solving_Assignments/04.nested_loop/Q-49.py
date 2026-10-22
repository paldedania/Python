# Q49. Factors of Every Number
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
for number in range(1, n + 1):
    factors = ""
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            if factors:
                factors += " "
            factors += str(divisor)
    print(number, "->", factors)
