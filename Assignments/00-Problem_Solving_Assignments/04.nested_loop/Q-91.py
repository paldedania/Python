# Q91. Word Pair With Maximum Common Characters
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
words = input().split()
best_score = -1
pair = ""
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        shared = ""
        for a in words[i]:
            for b in words[j]:
                if a == b and a not in shared:
                    shared += a
        if len(shared) > best_score:
            best_score = len(shared)
            pair = words[i] + " " + words[j]
print(pair if pair else "Need two words")
if pair:
    print("Distinct common characters =", best_score)
