sentence = input("Enter a sentence: ")
character = input("Enter a character to count: ")

print("Original Sentence:", sentence)
print("Number of Characters:", len(sentence))
print("Number of Words:", len(sentence.split()))

if sentence:
    print("First Character:", sentence[0])
    print("Last Character:", sentence[-1])
else:
    print("First Character: The sentence is empty.")
    print("Last Character: The sentence is empty.")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title Case:", sentence.title())
print("Python Exists:", "Python" in sentence)
print("Chosen Character Count:", sentence.count(character))
