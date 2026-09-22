# variables used
name = input("Enter a input having upper lower case letters then digits then spaces and special characters. \n")
count_Upper = 0
count_Lower = 0
count_space = 0
count_digits = 0
count_special_char = 0
double = 0
cat = 0
result = 0
count = []

# using for loop to get the count
for i in name:
    if i >= "A" and i<="Z":
        count_Upper+=1
    elif i >= "a" and i<="z":
        count_Lower+=1
    elif i >= "0" and i<="9":
        count_digits+=1
    elif i== " ":
        count_space+=1
    else:
        count_special_char+=1

# Adding count to a list

count.append(count_Upper)
count.append(count_Lower)
count.append(count_special_char)
count.append(count_space)
count.append(count_digits)

# checking for the highest

for i in range(len(count)):
    if count[i] > result:
        result = count[i]
        cat = i
    elif count[i]==result:
        double+=1

# printing the value
if double == 0:
    if cat ==0:
        print("its Uppercase")
    elif cat==1:
        print("its Lowercase")
    elif cat==2:
        print("its special_chat")
    elif cat==3:
        print("its space")
    elif cat==4:
        print("its digits")
else:
    print("tie")

