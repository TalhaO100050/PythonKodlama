#Soru 1
def ciftTek(sayi):
    if sayi%2 == 0:return "çift"
    else:return "tek"


x = int(input("Bir sayı giriniz: "))
print(ciftTek(x))
#----------------------------------------------------------------#
print()
print()
#----------------------------------------------------------------#
#Soru 2
def pozitifNegatif(sayi):
    if sayi > 0:return "pozitif"
    elif sayi < 0:return "negatif"
    else:return "nötr"


x = int(input("Bir sayı giriniz: "))
print(pozitifNegatif(x))
#----------------------------------------------------------------#
print()
print()
#----------------------------------------------------------------#
#Soru 3
def vicutKitleIndeks(boy,kilo):
    vctKtlIndks = kilo / boy**2
    if vctKtlIndks < 18:return"zayıf"
    elif vctKtlIndks < 25:return "nornal"
    elif vctKtlIndks < 30:return "kilolu"
    elif vctKtlIndks < 35:return "obez"
    else:return "ciddi obez"


x = float(input("Boyunuzu giriniz(m): "))
y = int(input("Kilonuzu giriniz(kg): "))
print(vicutKitleIndeks(x,y))
#----------------------------------------------------------------#
print()
print()
#----------------------------------------------------------------#
#Soru 4
print(*range(1,21),sep="\n")
#----------------------------------------------------------------#
print()
print()
#----------------------------------------------------------------#
#Soru 5
for i in range(1,21):
    if i % 2 == 0:
        print(i)
#----------------------------------------------------------------#
print()
print()
#----------------------------------------------------------------#
#Soru 6
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
#----------------------------------------------------------------#
print()
print()
#----------------------------------------------------------------#
#Soru 7
def araSayılarToplam(sayi1,sayi2):
    toplam = 0
    if sayi1 > sayi2:bSayi = sayi1;kSayi = sayi2
    elif sayi1 < sayi2:bSayi = sayi2;kSayi = sayi1
    else:return "0"
    for i in range(kSayi,(bSayi+1)):
        toplam = toplam + i
    return toplam


x = int(input("Bir sayı giriniz: "))
y = int(input("Bir sayı daha giriniz: "))
print(araSayılarToplam(x,y))
#----------------------------------------------------------------#
print()
print()
#----------------------------------------------------------------#
#Soru 8
toplamf = 0
z = 0
print("Kaç kişisiniz?")
a = int(input())
while a < 1:
    print("Pozitif bir sayı giriniz.")
    a = int(input())
print("Bilet fiyatları")
print("Sinema bileti 15TL")
print("Tiyatro bileti 10TL")
while not z == "s" and not z == "t":
    print("Hangisine gitmek istiyorsun?(s/t)")
    z = input()
for i in range(1,a+1):
    x = 0
    y = 0
    toplam = 0
    print("Kişi",i)
    while not x == "e" and not x == "h":
        print("7 ya şından küçük müsün?(e/h)")
        x = input()
    while not y == "e" and not y == "h" and x == "h":
        print("Öğrenci misin?(e/h)")
        y = input()
    print()

    if z == "s":toplam += 15
    else:toplam += 10
    if x == "e":toplam = 0
    if y == "e":toplam = toplam / 2
    toplamf += toplam
print("Tutar :",toplamf,"TL")
#----------------------------------------------------------------#
print()
print()
#----------------------------------------------------------------#
#Soru 9
def alanHesapla(x,y,ne):
    if ne == "çevre":
        print((x*2)+(y*2))
    if ne == "alan":
        print(x*y)


x = int(input("Dikdörtgenin birinci uzunluğu: "))
y = int(input("Dikdörtgenin ikinci uzubluğu: "))
ne = input("(alan,çevre)")
alanHesapla(x,y,ne)
    
















