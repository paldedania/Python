name = input("enter a string: ")
lis = []
score = 1
for i in name:
    if i in lis:
        score +=1
        print(i)
    else:
        lis.append(i)

if score == 2:
    print("its a duplicate")
elif score <=4:
    print("its Repeated")
elif score > 4:
    print("Highly Reapated")