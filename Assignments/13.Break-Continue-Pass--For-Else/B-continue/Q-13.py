                                                    
text = input("Enter a string: ")
target = input("Enter the character to remove from display: ")

for character in text:
    if character == target:
        continue
    print(character, end="")
print()
