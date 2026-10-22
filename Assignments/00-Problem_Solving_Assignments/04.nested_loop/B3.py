# B3. Word Pair Analyzer
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
words = input().split()
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        common = False
        for a in words[i]:
            for b in words[j]:
                if a == b:
                    common = True
        if len(words[i]) == len(words[j]) and common:
            print(words[i], words[j])
