num = int(input("enter your number: "))
count = 0
for i in range(2,num):
    if num%i ==0:
        # print(f"{num} not  a prime number as it is also divisible by {i}")
        count += 1

if count == 0:
    print("its a prime number")
else:
    print("its not a prime number")