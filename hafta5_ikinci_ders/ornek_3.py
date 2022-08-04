sayac = 0
while sayac < 10:
    print("Hello World")
    sayac = sayac + 1

print()

ad = input("Adınızı giriniz: ")
sayac = 0
while sayac < 10:
    print("Merhaba",ad)
    sayac = sayac + 1

print()

a = 1
while a <= 1000:
    if a % 3 == 0:
        print(a,end=",")
    a=a+1

print()
print()

liste = []
a = 1
while a <= 1000:
    if a % 3 == 0:
        liste.append(a)
    a=a+1
print(len(liste))

print()

liste = []
a = 1
while a <= 1000:
    if a % 8 == 0 and a % 3 == 0:
        liste.append(a)
    a=a+1
print(len(liste))

print()

a = 0
b = 0
while a <= 100:
    if a % 3 == 0:
        b = b + a
    a=a+1
print(b)
