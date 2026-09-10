text = input("Enter a string: ")
count = 0

for character in text:
    if character >= "A" and character <= "Z":
        count = count + 1

print(count)
