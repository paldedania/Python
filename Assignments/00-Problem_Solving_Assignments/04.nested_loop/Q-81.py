# Q81. Remove Duplicate Characters
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
text = input()
result = ""
for ch in text:
    exists = False
    for previous in result:
        if ch == previous:
            exists = True
    if not exists:
        result += ch
print(result)
