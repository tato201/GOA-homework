age = int(input("Enter your age: "))
heart_rate = int(input("Enter your heart rate: "))

if age < 30 and heart_rate < 140:
    print("You can exercise more")
elif age >= 30 and heart_rate > 170:
    print("You need to rest")
else:
    print("Activity level is normal")