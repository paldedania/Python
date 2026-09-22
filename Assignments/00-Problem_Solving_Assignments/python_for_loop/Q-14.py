words = input("Enter a sentance: ").split()
vowels = ["a","e","i","o","u"]
consonants = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
]
sv =0
sc =0
for i in words:
    for j in i:
        if j in vowels:
            sv +=1
        elif j in consonants:
            sc +=1
    if sv>sc:
        print("Vowel Heavy")
    elif sc>sv:
        print("Consonant Heavy")
    else:
        print("Balanced")