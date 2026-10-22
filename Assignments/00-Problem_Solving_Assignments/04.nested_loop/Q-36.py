# Q36. Compare Words
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
words = input().split()
for i in range(len(words)):
    for j in range(len(words)):
        a = words[i]
        b = words[j]
        print(a, b)
