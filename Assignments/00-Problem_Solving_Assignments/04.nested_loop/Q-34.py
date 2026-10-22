# Q34. ASCII Difference
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
text = input()
# Outer loop selects the first position; inner loop selects the second.
for i in range(len(text)):
    for j in range(len(text)):
        a = text[i]
        b = text[j]
        if i != j:
            print(a, b, "->", abs(ord(a) - ord(b)))
