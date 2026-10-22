# Q82. Anagram Checker
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
first = input()
second = input()
anagram = len(first) == len(second)
for ch in first:
    first_count = 0
    second_count = 0
    for other in first:
        if ch == other:
            first_count += 1
    for other in second:
        if ch == other:
            second_count += 1
    if first_count != second_count:
        anagram = False
print("Anagram" if anagram else "Not anagram")
