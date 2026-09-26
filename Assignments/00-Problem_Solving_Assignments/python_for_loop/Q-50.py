inputs = []
scores = []
vowel_totals = []
digit_totals = []
total_vowels = 0
total_consonants = 0
total_digits = 0
total_spaces = 0
total_special = 0

for i in range(10):
    text = input("Enter text: ")
    inputs.append(text)
    uppercase = 0
    lowercase = 0
    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0
    special = 0
    score = 0
    longest_word = ""

    for word in text.split():
        if len(word) > len(longest_word):
            longest_word = word

    repeated_characters = []
    checked_characters = []
    for char in text:
        if "A" <= char <= "Z":
            uppercase += 1
        elif "a" <= char <= "z":
            lowercase += 1

        if char in "aeiouAEIOU":
            vowels += 1
            score += 2
        elif ("a" <= char <= "z") or ("A" <= char <= "Z"):
            consonants += 1
            score += 1
        elif "0" <= char <= "9":
            digits += 1
            score += 3
        elif char == " ":
            spaces += 1
        else:
            special += 1
            score += 4

        if char not in checked_characters:
            frequency = 0
            for other_char in text:
                if char == other_char:
                    frequency += 1
            if frequency > 1:
                repeated_characters.append(char)
            checked_characters.append(char)

    print("Input", i + 1)
    print("Uppercase:", uppercase, "Lowercase:", lowercase)
    print("Vowels:", vowels, "Consonants:", consonants)
    print("Digits:", digits, "Spaces:", spaces, "Special:", special)
    print("Longest word:", longest_word)
    print("Repeated characters:", len(repeated_characters))
    print("Score:", score)

    scores.append(score)
    vowel_totals.append(vowels)
    digit_totals.append(digits)
    total_vowels += vowels
    total_consonants += consonants
    total_digits += digits
    total_spaces += spaces
    total_special += special

highest_score = scores[0]
highest_vowels = vowel_totals[0]
highest_digits = digit_totals[0]
score_input = inputs[0]
vowel_input = inputs[0]
digit_input = inputs[0]

for i in range(1, len(inputs)):
    if scores[i] > highest_score:
        highest_score = scores[i]
        score_input = inputs[i]
    if vowel_totals[i] > highest_vowels:
        highest_vowels = vowel_totals[i]
        vowel_input = inputs[i]
    if digit_totals[i] > highest_digits:
        highest_digits = digit_totals[i]
        digit_input = inputs[i]

print("Input with highest score:", score_input)
print("Input with most vowels:", vowel_input)
print("Input with most digits:", digit_input)
print("Total vowels:", total_vowels)
print("Total consonants:", total_consonants)
print("Total digits:", total_digits)
print("Total special characters:", total_special)

text_total = total_vowels + total_consonants
highest_category = text_total
classification = "Text Heavy"
if total_digits > highest_category:
    highest_category = total_digits
    classification = "Number Heavy"
elif total_digits == highest_category:
    classification = "Balanced"
if total_special > highest_category:
    highest_category = total_special
    classification = "Special Character Heavy"
elif total_special == highest_category:
    classification = "Balanced"

print("Overall classification:", classification)
