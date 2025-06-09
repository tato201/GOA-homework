age = int(input("Enetr your age: "))

if age < 0:
    print("wrong age")
elif age < 13:
    print('your are child')
elif 13 < age <= 19:
    print("teen")
elif 20 <= age <= 59:
    print('adult')
elif age >= 60:
    print("pensioner")