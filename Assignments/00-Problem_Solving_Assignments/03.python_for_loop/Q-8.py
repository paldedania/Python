budget = 0
regular = 0
premium = 0
luxury = 0
total = 0

for i in range(8):
    price = float(input("Enter the price: "))
    total += price
    if price < 500:
        budget += 1
        print("Budget")
    elif price <= 1999:
        regular += 1
        print("Regular")
    elif price <= 4999:
        premium += 1
        print("Premium")
    else:
        luxury += 1
        print("Luxury")

print("Budget products:", budget)
print("Regular products:", regular)
print("Premium products:", premium)
print("Luxury products:", luxury)
print("Total amount:", total)
print("Average price:", total / 8)
