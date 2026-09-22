# variables used
name = input("Enter a password \n")
count_Upper = 0
count_Lower = 0
count_digits = 0
count_special_char = 0

count = []

# using for loop to get the count
for i in name:
    if i >= "A" and i<="Z":
        count_Upper+=1
    elif i >= "a" and i<="z":
        count_Lower+=1
    elif i >= "0" and i<="9":
        count_digits+=1
    else:
        count_special_char+=1

total = count_digits+count_Lower+count_special_char+count_Upper

per1 = (count_Upper/total)*100
per2 = (count_Lower/total)*100
per3 = (count_digits/total)*100
per4 = (count_special_char/total)*100

print(f"percentage of upperchars is {per1} then of lowercahars is {per2} then of digits is {per3} then of special char is {per4}")
