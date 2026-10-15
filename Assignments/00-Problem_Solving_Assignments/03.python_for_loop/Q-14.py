words = input("Enter a sentence: ").split()

for word in words:
    vowels = 0
    consonants = 0
    for char in word.lower():
        if char in "aeiou":
            vowels += 1
        elif "a" <= char <= "z":
            consonants += 1

    if vowels > consonants:
        result = "Vowel Heavy"
    elif consonants > vowels:
        result = "Consonant Heavy"
    else:
        result = "Balanced"
    print(word, result)
