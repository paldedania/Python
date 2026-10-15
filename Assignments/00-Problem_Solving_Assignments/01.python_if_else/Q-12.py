character = input("Enter one character: ")

if character >= "A" and character <= "Z":
    print("Uppercase alphabet")
elif character >= "a" and character <= "z":
    print("Lowercase alphabet")
elif character >= "0" and character <= "9":
    print("Digit")
else:
    print("Special character")
