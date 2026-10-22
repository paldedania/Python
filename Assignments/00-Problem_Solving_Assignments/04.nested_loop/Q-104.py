# Q104. Reverse Word Pyramid
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
words = input().split()
# Outer loop selects a row; inner loop produces its columns.
for row in range(len(words), 0, -1):
    line = ""
    for col in range(row):
        if line:
            line += ' '
        line += str(words[col])
    print(line)
