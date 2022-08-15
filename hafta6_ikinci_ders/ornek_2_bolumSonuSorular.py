#Soru 1
asal = 0
a = int(input("Bir sayı giriniz. "))
if not a == 1:
    for i in range(2,a):
        if a % i == 0:
            asal = 1
            if i == 1 and i == a:
                asal = 0
    if asal == 1:print("Bu sayı asal değildir.")
    else:print("Bu sayı asaldır.")
else:print("Bu sayı asal değildir.")
#------------------------------------------------------#
print()
print()
#------------------------------------------------------#
#Soru 2
bosluk = 0
a = int(input("Pozitif bir sayı giriniz. "))
while a >= 1:
    b = a
    print(bosluk*" ",end="")
    while b >= 1:
        print("1",end=" ")
        b -= 1
    bosluk += 1
    print()
    a -= 1
#------------------------------------------------------#
print()
print()
#------------------------------------------------------#
#Soru 3
liste = []
while True:
    a = (input("Bir sayı giriniz durmak için (x) yazınız :"))
    if a == "x":
        break
    else:
        liste.append(int(a))
liste.sort()
print("En küçük sayı",liste[0],"en büyük sayı",liste[len(liste)-1])
#------------------------------------------------------#
print()
print()
#------------------------------------------------------#
#Soru 4
liste1 = []
liste2 = []
liste3 = []
while True:
    a = input("Birinci listeye eklenicek değerleri giriniz bitirmek için (x) yazınız. ")
    if a == "x":
        break
    liste1.append(a)
while True:
    a = input("İkinci listeye eklenicek değerleri giriniz bitirmek için (x) yazınız. ")
    if a == "x":
        break
    liste2.append(a)
sayac = 0
while sayac < len(liste1):
    liste3.append(liste1[sayac])
    sayac += 1
sayac = 0
while sayac < len(liste2):
    liste3.append(liste2[sayac])
    sayac += 1
print ("Liste 3:",liste3)
#------------------------------------------------------#
print()
print()
#------------------------------------------------------#
#Soru 5
b = ""
print("Bir cümle yazınız:")
a = input()
for i in a:
    if not i == " ":
        b = b + i    
print("Boşluksuz:",b)
































