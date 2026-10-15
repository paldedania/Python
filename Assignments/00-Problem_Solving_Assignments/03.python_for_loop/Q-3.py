sentence = input("Enter your sentence: ")
words = sentence.split()
highest_word = ""
highest_score = 0

for word in words:
    score = 0
    for char in word:
        if char in "aeiouAEIOU":
            score += 2
        elif "0" <= char <= "9":
            score += 3
        elif ("a" <= char <= "z") or ("A" <= char <= "Z"):
            score += 1
        else:
            score += 4

    print(word, "score:", score)
    if score > highest_score:
        highest_score = score
        highest_word = word

print("Word with highest score:", highest_word)
print("Highest score:", highest_score)
