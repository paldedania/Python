# B1. Perfect-Square Pair
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
for a in range(1, n + 1):
    for b in range(1, n + 1):
        square = False
        for root in range(1, a * b + 1):
            if root * root == a * b:
                square = True
                break
        if square:
            print(a, b)
