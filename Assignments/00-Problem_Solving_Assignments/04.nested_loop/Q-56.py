# Q56. Pair With Target Sum
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
target = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j == target:
            print(i, j)
