# Q24. Character Matching
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
first = input()
second = input()
for a in first:
    for b in second:
        if a == b:
            print(a, b)
