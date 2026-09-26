text = input("Enter a word or sentence: ")
result = ""

for char in text:
    if char in "aeiouAEIOU":
        result += "@"
    elif ("a" <= char <= "z") or ("A" <= char <= "Z"):
        result += char.lower()
    elif "0" <= char <= "9":
        result += "#"
    elif char == " ":
        result += "_"
    else:
        result += "!"

print("Transformed password:", result)
