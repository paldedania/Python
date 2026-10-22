# Q70. Number and Character Grid
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
word = input()
n = int(input())
# Outer loop selects a row; inner loop produces its columns.
for row in range(len(word)):
    line = ""
    for col in range(1, n + 1):
        if line:
            line += ' '
        line += str(word[row] + str(col))
    print(line)
