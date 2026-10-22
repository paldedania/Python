# Q28. Common Characters
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
first = input()
second = input()
seen = ""
for a in first:
    for b in second:
        if a == b and a not in seen:
            print(a)
            seen += a
