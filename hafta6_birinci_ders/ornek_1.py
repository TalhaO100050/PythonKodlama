sayac = 1
while sayac <= 100:
    if sayac % 2 == 0:
        print(sayac, end=",")
    sayac += 1
print()
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
toplam = 0
sayac = 1
while sayac <= 100:
    if sayac % 2 == 0:
        toplam += sayac
    sayac += 1
print("Sayıların toplamı :",toplam)
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
i = 1
while True:
    print(i)
    i = i + 1
    if i == 6:
        break
print("Döngü sonlandırıldı")
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
liste = []
print("Sonlandırmak için q yazınız.")
while 1:
    urun = input("Ürün adı giriniz :")
    if urun == "q":
        break
    liste.append(urun)
print("Listeniz :",liste)
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
tahmin = 0
while True:
    print("1-100 arasında bir sayı söyleyiniz")
    sayi = int(input("Sayı :"))
    if sayi == 61:
        tahmin += 1
        break
    elif sayi < 61:
        tahmin += 1
        print("Daha büyük bir sayı giriniz.")
    elif sayi > 61:
        tahmin += 1
        print("Daha küçük bir sayı giriniz.")
print("Tebrikler kazandın.")
print("Tahmin sayısı",tahmin)
#----------------------------------------------------#
print()
print()
#----------------------------------------------------#
toplam = 1
sayac = 1
sayi = int(input("Sayı giriniz :"))
while sayac <= sayi:
    toplam = sayac * toplam
    sayac += 1
print(sayi,"faktoriyel =",toplam)





























