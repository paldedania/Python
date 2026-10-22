# Q79. Duplicate Character Detector
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
text = input()
seen = ""
for ch in text:
    if ch not in seen:
        seen += ch
        frequency = 0
        for other in text:
            if other == ch:
                frequency += 1
        if frequency > 1:
            print(ch)
