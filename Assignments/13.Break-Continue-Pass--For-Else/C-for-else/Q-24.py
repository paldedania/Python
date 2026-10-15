                                             
n = int(input("Enter an integer (2 or greater): "))

for divisor in range(2, n):
    if n % divisor == 0:
        print("Not prime")
        break
else:
    print("Prime")
