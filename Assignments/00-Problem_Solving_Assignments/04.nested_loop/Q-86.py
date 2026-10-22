# Q86. Palindrome Word Analyzer
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
words = input().split()
longest = ""
for word in words:
    palindrome = True
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            palindrome = False
    print(word, "Palindrome" if palindrome else "Not palindrome")
