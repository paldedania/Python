# 

string = input("enter your sentence \n").lower()
words = string.split()
i = ""
name = ""
vowels = ["a","e","i","o","u"]
consonants = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
]
score = []
s1 = 0
for i in words:
    for j in i:
        if j in vowels:
            s1 +=2
        elif j >= "0" and "9" <=j :
            s1 += 3
        elif j in consonants:
            s1 += 1
        else:
            s1 += 4
    score.append(s1)

print(f"total score is {score}")