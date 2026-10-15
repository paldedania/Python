character = input("Enter one character: ")

if (character >= "A" and character <= "Z") or (character >= "a" and character <= "z"):
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u" or character == "A" or character == "E" or character == "I" or character == "O" or character == "U":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")
