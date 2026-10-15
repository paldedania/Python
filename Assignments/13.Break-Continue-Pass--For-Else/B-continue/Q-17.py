                                           
word = input("Enter a word: ")
count = 0

for character in word.lower():
    if character in "aeiou":
        continue
    count += 1

print(count)
