age = int(input("Enter your age: "))

if age <= 12:
    print("Eat foods rich in vitamins")
elif age <= 25:
    print("Eat energy-rich foods")
elif age <= 59:
    print("Maintain a balanced diet")
else:  # age >= 60
    print("Low-calorie and light food is recommended")