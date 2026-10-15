names = []
quantities = []
out_of_stock = 0
critical = 0
low = 0
available = 0

for i in range(8):
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    names.append(name)
    quantities.append(quantity)

    if quantity == 0:
        print("Out of Stock")
        out_of_stock += 1
    elif quantity <= 5:
        print("Critical")
        critical += 1
    elif quantity <= 20:
        print("Low")
        low += 1
    else:
        print("Available")
        available += 1

highest_quantity = quantities[0]
for quantity in quantities:
    if quantity > highest_quantity:
        highest_quantity = quantity

print("Out of Stock:", out_of_stock)
print("Critical:", critical)
print("Low:", low)
print("Available:", available)
print("Product(s) with highest quantity:")
for i in range(len(names)):
    if quantities[i] == highest_quantity:
        print(names[i], highest_quantity)
