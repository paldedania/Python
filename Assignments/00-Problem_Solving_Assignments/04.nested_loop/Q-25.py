# Q25. Count Matching Characters
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
first = input()
second = input()
matches = 0
for a in first:
    for b in second:
        if a == b:
            matches += 1
print(matches)
