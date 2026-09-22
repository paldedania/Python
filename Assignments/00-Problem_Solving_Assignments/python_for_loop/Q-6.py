test = 0
digit = 0
num = 0
string =""
even_count = 0
odd_count = 0
for i in range(5):
    num = int(input("Whats your number: "))
    string = str(num)
    print(f"your number is {num}")
    test = num
    while test >0:
        digit = test % 10
        if digit%2==0:
            even_count +=1
        else:
            odd_count +=1
        test = test//10
    print(f"its string is {string} and even count of that number is {even_count} and its odd count is {odd_count}")
    if odd_count == even_count:
        print("its equal odd and even")
    elif odd_count >= even_count:
        print("odd are more")
    else:
        print("even are more")
