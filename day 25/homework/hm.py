# ჩაშენებული ფუნქციები (Built-in Functions) — Python-ში არსებული სტანდარტული ფუნქციები, რომლებიც დამატებითი ბიბლიოთეკების გარეშე ხელმისაწვდომია

# print() - ბეჭდავს ეკრანზე ინფორმაციის გამოყვანას
# len() - აბრუნებს ელემენტების რაოდენობას სიისთვის, სტრინგისთვის და სხვა კოლექციებისთვის
# type() - აბრუნებს მონაცემის ტიპს
# int() - სტრიქონს ან სხვა ტიპს გარდაქმნის მთელ რიცხვად (თუ შესაძლებელია)
# str() - გარდაქმნის მონაცემს სტრინგად
# input() - მომხმარებლისგან იღებს შეყვანილ ტექსტს (სტრინგის სახით)
# range() - ქმნის რიცხვების თანმიმდევრობას (მრავალჯერადი გამოყენებისთვის ციკლში)

# ფუნქცია იქმნება def საკვანძო სიტყვით. შემდეგ ეწერება ფუნქციის სახელი. შემდეგ ფრჩხილებში თუ არის საჭირო იწერება არგუმენდტი
# ბოლოს უნდა იდოს ორ წერტილი (:)
# ფუნქციის შიგნით არსებული კოდი აუცილებლად უნდა იყოს ჩანაცვლებული (indentation)

# def ფუნქციის_სახელი(არგუმენტი1, არგუმენტი2):
#     # ეს კოდი შესრულდება ფუნქციის გამოძახებისას
#     # შეგვიძლია რამე ვბეჭდოთ ან გამოვთვალოთ
#     print("ეს ფუნქცია მუშაობს")

# # ფუნქციის გამოძახება:
# ფუნქციის_სახელი(მნიშვნელობა1, მნიშვნელობა2)
# ფუნქციის განსაზღვრა

def greet(name):
    print("გამარჯობა, " + name + "! მიხარია შენი ნახვა.") 