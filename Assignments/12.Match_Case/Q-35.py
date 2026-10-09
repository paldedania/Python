category = int(input("Enter category (1=Starters, 2=Main Course, 3=Desserts, 4=Drinks): "))

match category:
    case 1:
        item = int(input("Choose starter (1=Soup, 2=Spring Roll, 3=Garlic Bread): "))
        match item:
            case 1:
                print("Soup Selected")
            case 2:
                print("Spring Roll Selected")
            case 3:
                print("Garlic Bread Selected")
            case _:
                print("Invalid Starter")
    case 2:
        item = int(input("Choose main course (1=Pizza, 2=Pasta, 3=Biryani): "))
        match item:
            case 1:
                print("Pizza Selected")
            case 2:
                print("Pasta Selected")
            case 3:
                print("Biryani Selected")
            case _:
                print("Invalid Main Course")
    case 3:
        item = int(input("Choose dessert (1=Ice Cream, 2=Cake, 3=Gulab Jamun): "))
        match item:
            case 1:
                print("Ice Cream Selected")
            case 2:
                print("Cake Selected")
            case 3:
                print("Gulab Jamun Selected")
            case _:
                print("Invalid Dessert")
    case 4:
        item = int(input("Choose drink (1=Coffee, 2=Tea, 3=Juice): "))
        match item:
            case 1:
                print("Coffee Selected")
            case 2:
                print("Tea Selected")
            case 3:
                print("Juice Selected")
            case _:
                print("Invalid Drink")
    case _:
        print("Invalid Category")
