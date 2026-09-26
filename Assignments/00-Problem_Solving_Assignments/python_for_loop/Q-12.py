name = input("Enter the sentence: ")
vowels_count = 0
consonants_count = 0
vowel_frequency = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for char in name.lower():
    if char in "aeiou":
        vowels_count += 1
        vowel_frequency[char] += 1
    elif "a" <= char <= "z":
        consonants_count += 1

if vowels_count > consonants_count:
    print("Vowels Win")
elif consonants_count > vowels_count:
    print("Consonants Win")
else:
    print("Draw")

for vowel in vowel_frequency:
    print(vowel, vowel_frequency[vowel])
