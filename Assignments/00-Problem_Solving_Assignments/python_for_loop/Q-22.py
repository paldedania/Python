last_digit = ""
current_digit = ""
next_digit = ""
count = 1
name = input("Whats the string: ")
char = []
count_list = []
for i in name:
    current_digit =  i
    if last_digit == current_digit:
        count +=1
    else:
        char.append(i)
        last_digit = current_digit
        count_list.append(count)
        count = 1
count_list.append(count)

for i in range(0,min(len(count_list),len(char))):
    print(f"{char[i]}{count_list[i+1]}" ,end=" " )