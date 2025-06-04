#დავალება 1
n = int(input("enter your number: "))
i = 0
while i < n + 1:
    print(i)
    i += 1

#დავალება 2
while True:
    age = int(input('enter your age: '))
    card = input('do you have a student card: ')
    if age < 18 or card == "yes":
        print('u have savings')
    elif age>= 60:
        print("you have personal a discount")
    else:
        print('you dont have a discount')
    break

#დავალება 3
a = int(input('enter first numbr: '))
b =int(input('enter second number'))
if a > 0 and b > 0:
    print("both are positive")
elif (a > 0 and b <= 0) or (a >= 0 and b > 0):
    print("pne of them is positive")
else:
    print("none of them is positive")

#დავალება 4
while True:
    a = float(input("შეიყვანე პირველი რიცხვი: "))
    b = float(input("შეიყვანე მეორე რიცხვი: "))
    op = input("ოპერაცია (+, -, *, /): ")

    if op == "+":
        print("the result:", a + b)
    elif op == "-":
        print("the result:", a - b)
    elif op == "*":
        print("the result:", a * b)
    elif op == "/":
        if b != 0:
            print("the result:", a / b)
        else:
            print("Invalid operation! Cannot divide by zero.")
    else:
        print("wrong operation!")

