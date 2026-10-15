total_collection = 0

for passenger in range(8):
    age = int(input("Enter passenger age: "))
    distance = float(input("Enter distance in kilometers: "))
    fare = distance * 10

    if age < 5:
        fare = 0
        category = "Free"
    elif age <= 12:
        fare = fare / 2
        category = "50% discount"
    elif age >= 60:
        fare = fare * 70 / 100
        category = "30% discount"
    else:
        category = "Full fare"

    total_collection += fare
    print(category, "Fare:", fare)

print("Total collection:", total_collection)
