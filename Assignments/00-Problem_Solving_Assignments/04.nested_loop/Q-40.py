# Q40. Word Character Match
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
words = input().split()
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        a = words[i]
        b = words[j]
        shared = False
        for ch in a:
            for other in b:
                if ch == other:
                    shared = True
        if shared:
            print(a, b)
