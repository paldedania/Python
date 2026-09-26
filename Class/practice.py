same_char = 0
diff_char = 0
both_vowels = 0
both_digit = 0
vowels = ["a","e","i","o","u"]
digits = ["0","1","2","3","4","5","6","7","8","9"]

string = input("Enter a string: ").lower()

for i in range(len(string)):
    for j in range(i+1,len(string)):
        if string[i] == string[j]:
            same_char +=1
            j+=1
        else:
            diff_char += 1
        if string[i] and string[j] in vowels:
            both_vowels +=1
        elif string[i] and string[j] in digits:
            both_digit +=1

print(f"same characters are {same_char} then diff char are {diff_char} then both vowels are {both_vowels} then both digits are {both_digit}")·