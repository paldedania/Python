                                                                     
text = input("Enter a string: ")

for character in text:
    if text.count(character) >= 2:
        print(character)
        break
else:
    print("No repeated character")
