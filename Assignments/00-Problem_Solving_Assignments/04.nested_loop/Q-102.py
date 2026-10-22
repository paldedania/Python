# Q102. Character Pyramid
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
text = input()
for width in range(1, len(text) + 1):
    line = ""
    # Center prefixes with a single space between their characters.
    for space in range(len(text) - width):
        line += " "
    for col in range(width):
        if col:
            line += " "
        line += text[col]
    print(line)
