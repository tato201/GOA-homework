systolic = int(input("Enter systolic pressure: "))
diastolic = int(input("Enter diastolic pressure: "))

if systolic > 140 or diastolic > 90:
    print("High blood pressure")
elif systolic < 90 or diastolic < 60:
    print("Low blood pressure")
else:
    print("Blood pressure is normal")