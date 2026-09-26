first = input("Enter the first word: ")
second = input("Enter the second word: ")
shorter_length = len(first)
if len(second) < shorter_length:
    shorter_length = len(second)

pattern = ""
for i in range(shorter_length):
    if first[i] == second[i]:
        pattern += "S"
    else:
        pattern += "D"

print("Pattern:", pattern)
if len(first) > shorter_length:
    print("Extra characters in first word:", first[shorter_length:])
elif len(second) > shorter_length:
    print("Extra characters in second word:", second[shorter_length:])
else:
    print("There are no extra characters")
