text = input("Enter a string: ")
target = input("Enter the target character: ")

for character in text:
    print(character, end=" ")
    if character == target:
        break
print()
