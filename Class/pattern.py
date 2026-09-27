num = int(input("Enter your number:"))
i = 1
for j in range(1,num+1):
    while i <=10:
        print(i*j, end="\t")
        i+=1    
    i = 1
    print()
