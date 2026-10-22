# Q106. Character Frequency Pattern
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
        stars = ""
        for i in range(frequency):
            stars += "*"
        print(ch, stars)
