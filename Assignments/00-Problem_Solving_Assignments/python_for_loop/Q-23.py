Junior = 0
Mid = 0
Senior = 0
Executive = 0
salaries_list=[]
for i in range(8):
    salaries = int(input("What are your salaries?: "))
    if salaries<0:
        print("error its wrong this wont count")
    elif salaries >= 100000:
        print("Executive")
        Executive +=1
    elif salaries > 50000:
        print("Senior")
        Senior +=1
    elif salaries >= 25000:
        print("Mid")
        Mid+=1
    else:
        print("Junior")
        Junior+=1
    salaries_list.append(salaries)
print(f"in >100000 there are {Executive} then in >50000 there are {Senior} then in >25000 there are {Mid} then who <25000 are {Junior}")
total = 0
for i in range(len(salaries_list)):
    total += salaries_list[i]

avg = total / len(salaries_list)

print(f"avg saleroy is {avg}")