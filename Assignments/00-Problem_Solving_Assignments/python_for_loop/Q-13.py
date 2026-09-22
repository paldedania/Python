total = 0
price = 0
for i in range(6):
    units = int(input("Enter your units: "))

    if units>400:
        price += (units-400)*15
        price += (200*10)+(7*100)+(100*5)
    elif units>200:
        price += (units-200)*10
        price += (7*100)+(5*100)
    elif units>100:
        price += (units-100)*7
        price += 5*100
    elif units>0:
        price += units*5
    total += price
    print(f"price of {i} unit is {price}")
    if price>3000:
        print("High")
    elif price>1000:
        print("Medium")
    else:
        print("Low")

    price = 0
print(f"total revinue is {total}")