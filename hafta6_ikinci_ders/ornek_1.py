sayilar = [1,2,3,4,5]
kareler = []
for i in sayilar:
    kareler.append(i*i)
print(kareler)
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
sayac = 0
liste = []
liste2 = []
while 4 >= sayac:
    sayac += 1
    print("0 - 90 arası",sayac,". sayıyı giriniz :")
    a = int(input())
    liste.append(a)
for i in liste:
    liste2.append(90-i)
print("Sayıların tümlerleri :",liste2)
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
sayac = 0
liste = []
liste2 = []
while 4 >= sayac:
    sayac += 1
    print("0 - 90 arası",sayac,". sayıyı giriniz :")
    a = int(input())
    liste.append(a)
for i in liste:
    liste2.append(90-i)
liste2.sort()
print("Sayıların küçükten büyüğe tümlerleri :",liste2)
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
toplam = 0
liste1 = []
while True:
    a = input("Ortalamalarını bulmak istediğiniz sayıları giriniz(Durmak için dur yazınız) :")
    if a == "dur":
        break
    liste1.append(int(a))
for i in liste1:
    toplam += i
cevap = toplam / len(liste1)
print(cevap)
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
liste1 = []
liste2 = []
while True:
    a = input("Karelerini bulmak istediğiniz sayıları giriniz(Durmak için dur yazınız) :")
    if a == "dur":
        break
    liste1.append(int(a))
for i in liste1:
    liste2.append(i**2)
print(liste2)
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
liste1 = []
liste2 = []
while True:
    a = input("İstediğiniz sayıları giriniz(Durmak için dur yazınız) :")
    if a == "dur":
        break
    liste1.append(int(a))
for i in liste1:
    if i % 3 == 0:
        liste2.append(i)
print("Üçe bölünebilen sayılar :",liste2)
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
print(*range(10))
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
a = int(input("Tablobun satır uzunluğunu giriniz "))
b = int(input("Tablobun sütun uzunluğunu giriniz "))
for i in range(1,a+1):
    for j in range(1,b+1):
        print(j,end=" ")
    print()
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
print(*range(1,20,3))
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
dersler = ["Ders1","Ders2","Ders3"]
konular = ["Konu1","Konu2","Konu3"]
for x in dersler:
    for y in konular:
        print(x,y)
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
for i in range(1,6):
    if i == 2 or i == 4:
        continue
    print(i)
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#

























