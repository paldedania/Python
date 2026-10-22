# Q21. Character Repetition
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
text = input()
for ch in text:
    line = ""
    for repeat in range(3):
        line += ch
    print(line)
