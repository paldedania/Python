print("Choose a language: 1. English  2. Hindi")
choice1 = input("Enter your choice: ").strip().lower()

if choice1 == "1":
    choice1 = "english"
elif choice1 == "2":
    choice1 = "hindi"

match choice1:
    case "english":
        print("To book a product, press 1.")
        print("To get product information, press 2.")
        choice2 = input("Which service would you like? ").strip()

        match choice2:
            case "1":
                print("To book a plot, press 1. To book a house, press 2.")
                choice3 = input("What would you like to book? ").strip()

                match choice3:
                    case "1":
                        print("Your plot has been booked.")
                    case "2":
                        print("Your house has been booked.")
                    case _:
                        print("Invalid choice. Please select 1 or 2.")

            case "2":
                print("For product information, please contact our sales team.")
            case _:
                print("Invalid choice. Please select 1 or 2.")

    case "hindi":
        print("Product book karne ke liye 1 dabayein.")
        print("Product ki jaankari ke liye 2 dabayein.")
        choice2 = input("Aap kaunsi service chahte hain? ").strip()

        match choice2:
            case "1":
                print("Plot book karne ke liye 1 dabayein. Ghar book karne ke liye 2 dabayein.")
                choice3 = input("Aap kya book karna chahte hain? ").strip()

                match choice3:
                    case "1":
                        print("Aapka plot book ho gaya hai.")
                    case "2":
                        print("Aapka ghar book ho gaya hai.")
                    case _:
                        print("Galat choice. Kripya 1 ya 2 chunein.")

            case "2":
                print("Product ki jaankari ke liye hamari sales team se sampark karein.")
            case _:
                print("Galat choice. Kripya 1 ya 2 chunein.")

    case _:
        print("Invalid language choice. Please run the program again and choose 1 or 2.")
