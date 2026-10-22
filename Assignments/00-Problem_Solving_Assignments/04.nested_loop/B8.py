# B8. Smallest ASCII Difference
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
text = input()
smallest = None
pairs = []
for i in range(len(text)):
    for j in range(i + 1, len(text)):
        if text[i] != text[j]:
            difference = abs(ord(text[i]) - ord(text[j]))
            pair = text[i] + " " + text[j]
            if smallest is None or difference < smallest:
                smallest = difference
                pairs = [pair]
            elif difference == smallest and pair not in pairs:
                pairs.append(pair)
if smallest is None:
    print("Need two different characters")
else:
    print("Smallest difference =", smallest)
    for pair in pairs:
        print(pair)
