category = int(input("Enter category: "))

match category:
    case 1:
        food = int(input("Enter food: "))
        match food:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")
            case _:
                print("Invalid Vegetarian Food")
    case 2:
        food = int(input("Enter food: "))
        match food:
            case 1:
                print("Chicken Biryani Selected")
            case 2:
                print("Chicken Curry Selected")
            case 3:
                print("Fish Fry Selected")
            case _:
                print("Invalid Non-Vegetarian Food")
    case _:
        print("Invalid Category")
