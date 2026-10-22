# Q53. Common Factors
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
a = abs(int(input()))
b = abs(int(input()))
for first in range(1, a + 1):
    if a % first == 0:
        for second in range(1, b + 1):
            if b % second == 0 and first == second:
                print(first)
