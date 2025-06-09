age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))

if age < 10:
    if weight < 20:
        print("Weight is low")
    elif weight <= 40:
        print("Weight is normal")
    else:
        print("Weight is high")
elif 10 <= age <= 17:
    if weight < 40:
        print("Weight is low")
    elif weight <= 65:
        print("Weight is normal")
    else:
        print("Weight is high")
else:  # age >= 18
    if weight < 50:
        print("Weight is low")
    elif weight <= 90:
        print("Weight is normal")
    else:
        print("Weight is high")