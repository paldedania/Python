sentences = []
search_word = input("Enter the search word: ").lower()

for i in range(10):
    sentence = input("Enter a sentence: ")
    sentences.append(sentence)

total_occurrences = 0
for i in range(len(sentences)):
    words = sentences[i].lower().split()
    occurrences = 0
    for word in words:
        cleaned_word = ""
        for char in word:
            if ("a" <= char <= "z") or ("0" <= char <= "9"):
                cleaned_word += char
        if cleaned_word == search_word:
            occurrences += 1

    if occurrences > 0:
        print("Sentence", i + 1, "contains the word", occurrences, "time(s)")
    total_occurrences += occurrences

print("Total occurrences:", total_occurrences)
