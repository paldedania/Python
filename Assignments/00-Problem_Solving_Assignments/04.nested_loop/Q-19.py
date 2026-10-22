# Q19. Pair Product Filter
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j % 2 == 0:
            print(i, j, i * j)
