# Q80. First Repeated Character
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
text = input()
# First by original position, not by the time a second occurrence is seen.
for i in range(len(text)):
    repeated = False
    for j in range(i + 1, len(text)):
        if text[i] == text[j]:
            repeated = True
    if repeated:
        print(text[i])
        break
else:
    print("No repeated character")
