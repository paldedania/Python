sentence = input("Enter a sentence: ")

has_digit = False
has_dot = False
has_at = False
password_like = False
repeated_special = False

for char in sentence:
    if char >= "0" and char <= "9":
        has_digit = True
    elif char == ".":
        has_dot = True
    elif char == "@":
        has_at = True

words = sentence.lower().split()

for word in words:
    if "password" in word or "pass" in word or "pwd" in word:
        password_like = True

for i in range(len(sentence) - 1):
    first = sentence[i]
    second = sentence[i + 1]

    if first == second:
        if not (
            (first >= "a" and first <= "z")
            or (first >= "A" and first <= "Z")
            or (first >= "0" and first <= "9")
            or first == " "
        ):
            repeated_special = True

if password_like or repeated_special:
    classification = "Suspicious"
elif has_digit or has_dot or has_at:
    classification = "Review"
else:
    classification = "Safe"

print("Contains digits:", has_digit)
print("Contains URL-like dot:", has_dot)
print("Contains @:", has_at)
print("Contains password-like pattern:", password_like)
print("Contains repeated special characters:", repeated_special)
print("Security classification:", classification)