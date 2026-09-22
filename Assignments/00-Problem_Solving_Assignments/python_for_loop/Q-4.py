# variables
score_len = 0
score_uppercase = 0
score_lowercase = 0
score_one = 0
score_special = 0
score = 0
ans = []
for i in range(5):
    password = input("Whats your password: ")
    for j in password:
        if len(password) >= 8:
            score_len += 1
        if j>= "A" and j<="Z":
            score_uppercase +=1
        if j>="a" and j<="z":
            score_lowercase +=1
        if j>="0" and j<="9":
            score_one +=1
        if j.isalnum():
            score_special +=0
        else:
            score_special +=1
    score = score_special + score_one + score_lowercase +score_uppercase + score_len
    ans.append(score)
    score_len = score_uppercase = score_lowercase = score_one = score_special = score =0


for i in range(len(ans)):
    if ans[i] >=4:
        print("your  password was strong")
    elif ans[i] >=2:
        print("your  password was Medium")
    else:
        print("your  password was weak")