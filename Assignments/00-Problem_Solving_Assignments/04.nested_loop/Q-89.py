# Q89. Most Repeated Character
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
text = input()
best = ""
best_frequency = 0
seen = ""
for ch in text:
    if ch not in seen:
        seen += ch
        frequency = 0
        for other in text:
            if other == ch:
                frequency += 1
        if frequency > best_frequency:
            best_frequency = frequency
            best = ch
print(best if best else "No characters")
