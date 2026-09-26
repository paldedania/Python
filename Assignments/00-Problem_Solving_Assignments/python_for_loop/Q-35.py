sentence = input("Enter a sentence: ")
words = sentence.split()
longest = ""
shortest = ""
starts_with_vowel = 0
ends_with_vowel = 0
contains_digit = 0

for word in words:
    if len(longest) == 0 or len(word) > len(longest):
        longest = word
    if len(shortest) == 0 or len(word) < len(shortest):
        shortest = word

    if word[0] in "aeiouAEIOU":
        starts_with_vowel += 1
    if word[len(word) - 1] in "aeiouAEIOU":
        ends_with_vowel += 1

    word_has_digit = False
    for char in word:
        if "0" <= char <= "9":
            word_has_digit = True
    if word_has_digit:
        contains_digit += 1

print("Number of words:", len(words))
print("Number of characters:", len(sentence))
print("Longest word:", longest)
print("Shortest word:", shortest)
print("Words beginning with a vowel:", starts_with_vowel)
print("Words ending with a vowel:", ends_with_vowel)
print("Words containing digits:", contains_digit)
