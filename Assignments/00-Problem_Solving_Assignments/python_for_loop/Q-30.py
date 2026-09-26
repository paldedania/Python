text = input("Enter a string: ")
same = 0
different = 0
both_vowels = 0
both_digits = 0

for i in range(len(text)):
    for j in range(i + 1, len(text)):
        first = text[i]
        second = text[j]

        if first == second:
            same += 1
        else:
            different += 1

        if first in "aeiouAEIOU" and second in "aeiouAEIOU":
            both_vowels += 1
        if "0" <= first <= "9" and "0" <= second <= "9":
            both_digits += 1

print("Same character pairs:", same)
print("Different character pairs:", different)
print("Both vowels pairs:", both_vowels)
print("Both digits pairs:", both_digits)
