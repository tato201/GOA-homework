age = int(input("Enter your age: "))
hour = int(input("Enter the hour (0-23): "))

if age < 18 and hour >= 22:
    print("Time to sleep")
elif age >= 60 and hour >= 21:
    print("Rest is recommended")
else:
    print("You can continue your activity")