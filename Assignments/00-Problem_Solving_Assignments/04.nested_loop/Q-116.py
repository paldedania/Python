# Q116. Password Character Analyzer
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
password = input()
counts = [0, 0, 0, 0]
for ch in password:
    # Inner loop compares with the four ASCII character classes.
    for category in range(4):
        matches = (category == 0 and "A" <= ch <= "Z") or (category == 1 and "a" <= ch <= "z") or (category == 2 and "0" <= ch <= "9") or (category == 3 and not ("A" <= ch <= "Z" or "a" <= ch <= "z" or "0" <= ch <= "9"))
        if matches:
            counts[category] += 1
print("Uppercase =", counts[0], "Lowercase =", counts[1], "Digits =", counts[2], "Special =", counts[3])
