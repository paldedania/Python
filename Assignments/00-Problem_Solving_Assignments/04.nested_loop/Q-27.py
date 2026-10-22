# Q27. Vowel-Consonant Classification
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
text = input()
for ch in text:
    vowel = False
    for candidate in "AEIOUaeiou":
        if ch == candidate:
            vowel = True
    if vowel:
        print(ch, "= Vowel")
    elif ch.isalpha():
        print(ch, "= Consonant")
    else:
        print(ch, "= Not a letter")
