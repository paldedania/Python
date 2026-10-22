# Q54. Common Multiples
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
a = int(input())
b = int(input())
limit = int(input())
if a <= 0 or b <= 0:
    print("Use positive numbers")
else:
    for first in range(a, limit + 1, a):
        for second in range(b, limit + 1, b):
            if first == second:
                print(first)
