# Q83. Common Words
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
first = input().split()
second = input().split()
seen = []
for word in first:
    for other in second:
        if word == other and word not in seen:
            print(word)
            seen.append(word)
