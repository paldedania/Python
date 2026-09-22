budget = 0
regular = 0
premium = 0 
luxury = 0
price = 0
lis = []
total = 0
for i in range(5):
    price = int(input("Enter the price: "))
    if price<=500:
        budget += 1
    elif price<=1999:
        regular +=1
    elif price<=4999:
        premium +=1
    else:
        luxury +=1
    lis.append(price)
for i in range(len(lis)):
    total += lis[i]

avg = total/5

print(budget,regular,premium,luxury,total,avg,sep="\n")
