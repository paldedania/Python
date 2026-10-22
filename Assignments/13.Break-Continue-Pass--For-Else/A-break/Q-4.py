limit = int(input())
output = ""
for number in range(1, limit + 1):
    if number == 7:
        break
    if output:
        output += " "
    output += str(number)
print(output)
