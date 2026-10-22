# Q55. Pair With Greatest Product
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
if n < 1:
    print("No pairs")
else:
    best = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j > best:
                best = i * j
                first = i
                second = j
    print("Pair =", str(first) + "," + str(second))
    print("Product =", best)
