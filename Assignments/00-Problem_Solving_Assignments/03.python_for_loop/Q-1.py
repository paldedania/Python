name = input("Enter letters, digits, spaces and special characters: ")

count_upper = 0
count_lower = 0
count_digits = 0
count_spaces = 0
count_special = 0

for char in name:
    if "A" <= char <= "Z":
        count_upper += 1
    elif "a" <= char <= "z":
        count_lower += 1
    elif "0" <= char <= "9":
        count_digits += 1
    elif char == " ":
        count_spaces += 1
    else:
        count_special += 1

counts = [count_upper, count_lower, count_digits, count_spaces, count_special]
names = ["Uppercase letters", "Lowercase letters", "Digits", "Spaces", "Special characters"]
highest = 0
highest_name = ""
highest_count = 0

for i in range(len(counts)):
    if counts[i] > highest:
        highest = counts[i]
        highest_name = names[i]
        highest_count = 1
    elif counts[i] == highest:
        highest_count += 1

print("Uppercase:", count_upper)
print("Lowercase:", count_lower)
print("Digits:", count_digits)
print("Spaces:", count_spaces)
print("Special characters:", count_special)

if highest_count > 1:
    print("Tie")
else:
    print("Highest category:", highest_name)
