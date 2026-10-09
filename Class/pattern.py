i = 1

while i !=0:
    num = int(input("enter a number: "))
    print("choices for even is 1 then for  odd is 2 then for  prime is 3")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            if num%2 ==0:
                print("its even")
            else:
                print("its not even")
            i = 0
        case 2:
            if num%2 !=0:
                print("its odd")
            else:
                print("its not odd")
            i = 0
        case 3:
            count = 0
            for i in range(2,num):
                if num%i ==0:
                    count += 1
            if count == 0:
                print("its a prime number")
            else:
                print("its not prime")
            i = 0
        case _:
            print("wrong choice")
            i =1