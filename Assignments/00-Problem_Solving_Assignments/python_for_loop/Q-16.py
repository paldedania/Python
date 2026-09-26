name = input("Enter a password: ")
count_upper = 0
count_lower = 0
count_digits = 0
count_special = 0

for char in name:
    if "A" <= char <= "Z":
        count_upper += 1
    elif "a" <= char <= "z":
        count_lower += 1
    elif "0" <= char <= "9":
        count_digits += 1
    else:
        count_special += 1

total = len(name)
if total > 0:
    print("Uppercase percentage:", count_upper * 100 / total)
    print("Lowercase percentage:", count_lower * 100 / total)
    print("Digit percentage:", count_digits * 100 / total)
    print("Special percentage:", count_special * 100 / total)

counts = [count_upper, count_lower, count_digits, count_special]
names = ["Uppercase", "Lowercase", "Digits", "Special characters"]
highest = 0
category = ""
for i in range(len(counts)):
    if counts[i] > highest:
        highest = counts[i]
        category = names[i]
print("Dominant category:", category)
