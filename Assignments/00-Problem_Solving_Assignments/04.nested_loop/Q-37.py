# Q37. Same-Length Word Pairs
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
words = input().split()
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        a = words[i]
        b = words[j]
        if len(a) == len(b):
            print(a, b)
