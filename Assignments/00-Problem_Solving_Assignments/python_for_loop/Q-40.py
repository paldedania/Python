first = input("Enter the first string: ")
second = input("Enter the second string: ")
compatible = len(first) == len(second)
length = len(first)

if len(second) < length:
    length = len(second)

for i in range(length):
    first_char = first[i]
    second_char = second[len(second) - 1 - i]
    print(first_char, second_char)
    if first_char != second_char:
        compatible = False

if compatible:
    print("Mirror-compatible")
else:
    print("Not mirror-compatible")
