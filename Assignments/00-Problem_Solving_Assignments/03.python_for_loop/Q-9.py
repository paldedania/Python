text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special_characters = 0

for i in range(len(text)):
    char = text[i]

    if i % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    if char in "aeiouAEIOU":
        category = "vowel"
        vowels += 1
    elif ("a" <= char <= "z") or ("A" <= char <= "Z"):
        category = "consonant"
        consonants += 1
    elif "0" <= char <= "9":
        category = "digit"
        digits += 1
    else:
        category = "special character"
        special_characters += 1

    print(f"Character: {char!r}, Position: {i}, {parity}, Category: {category}")

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special_characters)