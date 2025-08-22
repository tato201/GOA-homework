# 1)კომენტარების სახით ჩამოწერეთ  ყველა პილიუსი და მინუსი set -ების
# პლიუსები - find აკეთებს უფრო ჩქარა შეუძლია გაერთიანება და თანაკვეთა და აგრეთვე გამოლლება და სისტემური გამოკლება.
# მინუსები - არ ალაგებს თანმიმდევრობით, არ შეგვიძლია ელემენტების ინდექსირება, 

# 2)შექენით სეტები და განიხილეთ ოპერატორები (union,intersection,difference,symmetric_difference,clear,add,remove) ახსენით ასევე კომენტარებით და გააკეთეთ ორივე ხერხით როგორც ტექსტიტ ისე სიმბოლოთი
A = {1,2,4,5,6,7}
B = {4,2,3,1,6}
print(A.union(B))
print(A | B)
#UNION აერთიანებს სეტებს

print(A.intersection(B))
print(A & B)
#intersection გვიჩვენებს სეტების თანაკვეთას ერთმანეთთან ანუ მათ შორის არსებულ ერთნაირ მონაცემებს

print(A.difference(B))
print(A - B)
#difference აკლებს ერთმანეს სეტებს

print(A.symmetric_difference(B))
print(A ^ B)
#symmetric_difference აკეთებს სიმეტრიკულ გამოკლებას სეტებში

A.add(12)
B.add(28)
print(A)
print(B)
#ამათებს სეტებში რაიმე ნებისმიერ მონაცემს

A.remove(12)
B.remove(28)
print(A)
print(B)
#აკლებს უკვე არსებულ სეტებში მყოფ მონაცემებს

A.clear
B.clear
print(A)
print(B)
#clear აქრობს ყველანაირ მონაცემს სეტებიდან

# 3)შექმენი სეტი fruit1 და fruit2 შეინახეთ სხვადასხვა ხილები და გააკეთეთ ყველა მანიპულაცია რაც გახსენდებათ ოპერატორების დახმარებით, შემდეგ ახხსენით კომენტარებით.
Fruit1 = {"ვაშლი", "ტყემალი", "ატამი", "მსხალი"}
Fruit2 = {"ვაშლატამა", "ბალი", "ალუბალი", "ლეღვი","ვაშლი"}

print(Fruit1.union(Fruit2))
print(Fruit1 | Fruit2)
#UNION აერთიანებს სეტებში არსებულ ხილებს

print(Fruit1.intersection(Fruit2))
print(Fruit1 & Fruit2)
#intersection საერთო ხილს გვიჩვენებს

print(Fruit1.difference(Fruit2))
print(Fruit1 - Fruit2)
#difference აკლებს ერთმანეს სეტებს

print(Fruit1.symmetric_difference(Fruit2))
print(Fruit1 ^ Fruit2)
#symmetric_difference აკეთებს სიმეტრიკულ გამოკლებას სეტებში

Fruit1.add("კარალიოკი")
Fruit2.add("მუშმალა")
print(Fruit1)
print(Fruit2)
#ამათებს სეტებში რაიმე ნებისმიერ მონაცემს

Fruit1.remove("კარალიოკი")
Fruit2.remove("მუშმალა")
print(Fruit1)
print(Fruit2)
#აკლებს უკვე არსებულ სეტებში მყოფ მონაცემებს

Fruit1.clear
Fruit2.clear
print(Fruit1)
print(Fruit2)
#clear აქრობს ყველანაირ მონაცემს სეტებიდან