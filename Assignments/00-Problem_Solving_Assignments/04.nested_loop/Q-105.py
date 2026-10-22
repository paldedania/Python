# Q105. Word Length Pattern
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
words = input().split()
for word in words:
    stars = ""
    for ch in word:
        stars += "*"
    print(word, stars)
