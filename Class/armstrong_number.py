num = int(input("Whats the number you wana check? \n"))
array = []
last_digit = None
test_num = num
while test_num > 0:
    last_digit = test_num % 10
    test_num = test_num //10
    array.append(last_digit)
    print(array)
    
array_length = len(array)

cube = num ** array_length
made_cube = 0
digit = 0


for i in range(array_length):
    digit = (array[i]**array_length)
    made_cube += digit**array_length
    print(made_cube)
    digit = made_cube = 0

print("Real cube is ", cube)
if cube == made_cube:
    print("True")
else:
    print("False")