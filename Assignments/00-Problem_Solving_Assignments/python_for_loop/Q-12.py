name = input("Whats the sentence: ")
vowels_count = 0
consonants_count = 0
vowels = ["a","e","i","o","u"]
consonants = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
]
for i in name:
    if i in vowels:
        vowels_count +=1
    elif i in consonants:
        consonants_count+=1

if consonants_count>vowels_count:
    print("consonants won")
elif consonants_count<vowels_count:
    print("vowels won")
else:
    print("Draw")
