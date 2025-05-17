#დავალება 1
i = 0
while i <= 10:
    print(i)
    i = i + 1

#დავალება 2
num = 10
while num >= 1:
    print(num)
    num -= 1

#დავალება 3
#while loop არის ციკლი როდესაც მოქმედება მეორდება ერთიდაიგივეჯერ იქამდე სანამა პირობა არის true და არ შეიცლება იგი false-ით

#დავალება 4 
password = "python123"
user_password = input('please enter your password: ')
while user_password != password:
    user_password = input('please try again your password: ')
print("ACCESS GRANTED")

#დავალება 5
n = int(input("enter your number: "))
p = 1
x = 0
while p <= n:
    x += p
    p += 1
print(x)

