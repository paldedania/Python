
sentence = input("Enter a sentence: ")
target = input("Enter the target word: ")

for word in sentence.split():
    if word == target:
        print("Found")
        break
else:
    print("Not found")
