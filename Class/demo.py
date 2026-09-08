num = int(input("Whats your number"))

f = num%10
num = num//10
s = num%10
num = num//10
t = num%10
num = num//10
if num == 0:
    print(f+s+t)
else:
    print("something is wrong")
