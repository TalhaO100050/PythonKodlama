#1.Soru

print("Bir sayı giriniz.")
sayi = int(input())
if sayi > 0:print("Pozitif bir sayı.")
elif sayi == 0:print("Sıfır.")
else:print("Negatif bir sayı.")

#------------------------------------------------------------#
print()
print()
print()
#------------------------------------------------------------#
#2.Soru

print("Sınav ortalamalarınızı giriniz.")
edebiyat = int(input("Edebiyat:"))
matematik = int(input("Matematik:"))
fizik = int(input("Fizik:"))
ortalamaPuan = (edebiyat + matematik + fizik) / 3
print("Ortalamanız",ortalamaPuan)

#------------------------------------------------------------#
print()
print()
print()
#------------------------------------------------------------#
#3.Soru

print("İki sayı giriniz.")
sayi1 = int(input("1.Sayı:"))
sayi2 = int(input("2.Sayı:"))
if sayi1 > sayi2:print(sayi1,sayi2,"den daha büyüktür.")
if sayi1 < sayi2:print(sayi2,sayi1,"den daha büyüktür.")
if sayi1 == sayi2:print("Sayılar eşittir.")

#------------------------------------------------------------#
print()
print()
print()
#------------------------------------------------------------#
#4.Soru

print("İki sayı giriniz.")
sayi1 = int(input("1.Sayı:"))
sayi2 = int(input("2.Sayı:"))
if sayi1 > sayi2:print(sayi1,sayi2,"den daha büyüktür.")
elif sayi1 < sayi2:print(sayi2,sayi1,"den daha büyüktür.")
else:print("Sayılar eşittir.")

#------------------------------------------------------------#
print()
print()
print()
#------------------------------------------------------------#
#5.Soru

print("Cevap 240")

#------------------------------------------------------------#
print()
print()
print()
#------------------------------------------------------------#
#6.Soru

print("Cevap 0")

#------------------------------------------------------------#
print()
print()
print()
#------------------------------------------------------------#
#7.Soru

print("1-4 arasında bir sayı giriniz.")
sayi1 = int(input())
if sayi1 == 1:print("İlkbahar")
if sayi1 == 2:print("Yaz")
if sayi1 == 3:print("Sonbahar")
if sayi1 == 4:print("Kış")

#------------------------------------------------------------#
print()
print()
print()
#------------------------------------------------------------#
#8.Soru

print("Dört tane uzunluk giriniz.")
u1 = int(input("Birnci uzunluk:"))
u2 = int(input("İkinci uzunluk:"))
u3 = int(input("Üçüncü uzunluk:"))
u4 = int(input("Dördüncü uzunluk:"))
if u1 == u2 and u2 == u3 and u3 == u4 and u4 == u1:print("Bu bir kare!")
elif u1 == u3 and u2 == u4:print("Bu bir dikdörtgen!")
elif u1 == u3 or u2 == u4:print("Bu bir yamuk!")
else:print("Bu bir dörtgen!")

#------------------------------------------------------------#
print()
print()
print()
#------------------------------------------------------------#
#9.Soru

print("Üç tane uznluk giriniz.")
u1 = int(input("Birnci uzunluk:"))
u2 = int(input("İkinci uzunluk:"))
u3 = int(input("Üçüncü uzunluk:"))
if u1 == u2 and u2 == u3:print("Bu bir eşkenarüçgen!")
elif u1 == u2 or u2 == u3 or u3 == u1:print("Bu bir ikizkenarüçgen!")
else:print("Bu bir üçgen!")

#------------------------------------------------------------#
print()
print()
print()
#------------------------------------------------------------#
#10.Soru

print("Beden kitle endeksinizi öğrenmek için boy ve kilonuzu giriniz.")
boy = int(input("Boy:"))
kilo = int(input("Kilo:"))
KE = kilo/(boy**2)
if KE < 18.5:print("Zayıf")
elif KE <= 25:print("Normal")
elif KE <= 30:print("Kilolu")
else:print("Obez")
