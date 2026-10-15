word = input("Enter a word: ")

for i in range(1, len(word) + 1):
    for j in range(i):
        print(word[j], end="")
    print()

print("Reverse pattern")
for i in range(len(word), 0, -1):
    for j in range(i):
        print(word[j], end="")
    print()
