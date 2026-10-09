category = int(input("Enter category: "))

match category:
    case 1:
        product = int(input("Enter product: "))
        match product:
            case 1:
                print("Mobile Selected")
            case 2:
                print("Laptop Selected")
            case 3:
                print("Headphones Selected")
            case _:
                print("Invalid Electronics Product")
    case 2:
        product = int(input("Enter product: "))
        match product:
            case 1:
                print("Shirt Selected")
            case 2:
                print("Jeans Selected")
            case 3:
                print("Shoes Selected")
            case _:
                print("Invalid Clothing Product")
    case _:
        print("Invalid Category")
