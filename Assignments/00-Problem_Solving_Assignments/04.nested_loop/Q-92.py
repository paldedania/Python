# Q92. Number Pair With Common Digits
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
first = str(abs(int(input())))
second = str(abs(int(input())))
common = ""
for a in first:
    for b in second:
        if a == b and a not in common:
            common += a
print("Common digit count =", len(common))
