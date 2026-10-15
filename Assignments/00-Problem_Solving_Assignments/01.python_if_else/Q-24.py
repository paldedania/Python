purchase_amount = float(input("Enter purchase amount: "))

if purchase_amount < 0:
    print("Invalid purchase amount")
else:
    if purchase_amount < 500:
        discount_percentage = 0
    elif purchase_amount < 1000:
        discount_percentage = 5
    elif purchase_amount < 2000:
        discount_percentage = 10
    elif purchase_amount < 5000:
        discount_percentage = 15
    else:
        discount_percentage = 20

    discount_amount = purchase_amount * discount_percentage / 100
    final_amount = purchase_amount - discount_amount

    print("Original amount:", purchase_amount)
    print("Discount percentage:", discount_percentage, "%")
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)
