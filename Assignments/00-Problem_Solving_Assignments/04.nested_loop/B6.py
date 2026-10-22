# B6. Maximum Word-Length Difference
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
words = input().split()
greatest = -1
pair = ""
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if words[i] != words[j]:
            difference = abs(len(words[i]) - len(words[j]))
            if difference > greatest:
                greatest = difference
                pair = words[i] + " " + words[j]
print(pair if pair else "Need two different words")
