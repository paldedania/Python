# Q88. Maximum Common Character
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
# Matching frequency means the number of equal cross-string position pairs.
# Keep the first character in the first string on ties.
first = input()
second = input()
best = ""
best_score = 0
seen = ""
for ch in first:
    if ch not in seen:
        seen += ch
        score = 0
        for a in first:
            if a == ch:
                for b in second:
                    if b == ch:
                        score += 1
        if score > best_score:
            best_score = score
            best = ch
print(best if best else "No common character")
print("Matching frequency =", best_score)
