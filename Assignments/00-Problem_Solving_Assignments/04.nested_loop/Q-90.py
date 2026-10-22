# Q90. Second Most Repeated Character
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
text = input()
highest = 0
second_highest = 0
second = ""
seen = ""
# Second means second distinct frequency. Ties keep first appearance.
for ch in text:
    if ch not in seen:
        seen += ch
        frequency = 0
        for other in text:
            if other == ch:
                frequency += 1
        if frequency > highest:
            second_highest = highest
            second = highest_character if highest else ""
            highest = frequency
            highest_character = ch
        elif second_highest < frequency < highest:
            second_highest = frequency
            second = ch
print(second if second else "No second distinct frequency")
