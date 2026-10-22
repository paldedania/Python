# B2. ASCII Difference Pair
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
text = input()
for a in text:
    for b in text:
        if abs(ord(a) - ord(b)) == 2:
            print(a, b)
