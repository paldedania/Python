                                       
text = input("Enter a string: ")
target = input("Enter the target character: ")

for character in text:
    if character == target:
        print("Character exists")
        break
else:
    print("Character missing")
