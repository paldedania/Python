# Q85. Unique Words
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
words = input().split()
seen = []
for word in words:
    if word not in seen:
        seen.append(word)
        frequency = 0
        for other in words:
            if other == word:
                frequency += 1
        if frequency == 1:
            print(word)
