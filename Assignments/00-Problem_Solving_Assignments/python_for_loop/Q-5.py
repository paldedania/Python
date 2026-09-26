sentence = input("Enter your sentence: ")
words = sentence.split()
short = 0
medium = 0
long = 0

for word in words:
    length = len(word)
    print(word, "length:", length)
    if length <= 3:
        print("Short")
        short += 1
    elif length <= 6:
        print("Medium")
        medium += 1
    else:
        print("Long")
        long += 1

print("Short words:", short)
print("Medium words:", medium)
print("Long words:", long)
