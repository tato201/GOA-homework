a = 1 
b = 0
c = 0
result_0 = (a and not b) or (b and not a)
result_1 = bool((b and c) and (a or b))
result_2 = (a and not c) or (b and not a) or (b and not c)
print(result_0)
print(result_1)
print(result_2)

# (a and not b) or (b and not a) აქ  პირველ რჩილებში მოცემული ოპერცია არის True  ხოლო მეორე ფრჩხილებში არსებული ოპერაცია არის False, True or False ში  როდესაც არის or ოპერატორი არის True.
# (b and c) and (a or b) პირველ ფრჩხილებში არსებული ოპერაცია გვიჩვენებს False ისევე როგორ მეორე ფრჩხილებში არსებული ოპერაცია გვიჩვენებს False რაც იმას ნიშნავს რომ and ოპერატორის დროს არის False.
# (a and not c) or (b and not a) or (b and not c) პურველ ფრჩხილში გვაქს True , მეორეში False, მესამეში False, აქედან დაგვრჩჰა (True or False) or False აქედან გამომდინარე გვრჩება True or False და or ოპერატორის გამო პასუხი არის True