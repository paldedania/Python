words = input("Enter a sentence: ").split()
secreat = input("Enter the secreate word: ")
count = 0
for i in range(len(words)):
    if secreat == words[i]:
        print("Secret word found")
        count +=1
if count == 0:
    print("secret word not found")