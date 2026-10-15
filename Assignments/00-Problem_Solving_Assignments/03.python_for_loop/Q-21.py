count_20 = 0
count_15 = 0
count_10 = 0
count_0 = 0

total_discount = 0
total_final_price = 0

for i in range(10):
    price = float(input("Enter product price: "))

    if price >= 5000:
        discount_rate = 20
        count_20 += 1
    elif price >= 3000:
        discount_rate = 15
        count_15 += 1
    elif price >= 1000:
        discount_rate = 10
        count_10 += 1
    else:
        discount_rate = 0
        count_0 += 1

    discount_amount = price * discount_rate / 100
    final_price = price - discount_amount

    total_discount += discount_amount
    total_final_price += final_price

    print("Discount:", discount_rate, "%")
    print("Discount amount:", discount_amount)
    print("Final price:", final_price)
    print()

print("Products with 20% discount:", count_20)
print("Products with 15% discount:", count_15)
print("Products with 10% discount:", count_10)
print("Products with no discount:", count_0)
print("Total discount:", total_discount)
print("Total final price:", total_final_price)