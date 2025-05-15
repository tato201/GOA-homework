#sequences - aris tanmimdevroba codis
print(5 + 1)
print(40 + 42)

#interation - aris gameoreba erti da igive moqmedebis
name = "gio"
print(name)
print(name)

#selection - gadawyvetilebis migeba
age = 24
if age >= 18:
    print("u are allowed")
else: 
    print("not allowed")

#algoritmi - moqmedebebis tanmimdevroba
num = 1
num2 = 2
num3 = num + num2
print(num + num2 + num3)

#4 davaleba
#pasuxi iqneba true radgan saboloo pasuxi gvrcheba true or false 

#4 davalebis 2 nawili
# 5 > 10 aris False
# 7 * 7 / 7 == 7 
# true and false = False

# true and false = false
# 7 + 9 + 1 = 17 false

number = int(input('choose a number '))
if( number % 2 == 0 and number > 10) or number == 7:
    print("true")

#davakeba 5
#INT
print(int('141'))
print(int(0.31))
print(int(True))
#STR
print(str('1231'))
print(str(123.1234))
print(str('false'))
#FLOAT
print(float(123))
print(float("43.123"))
print(float(True))
 
#davaleba 6
year = int(input('choose a year '))
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print("this is leap year")
