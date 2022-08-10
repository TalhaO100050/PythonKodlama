yazi = "Python üst düzey basit sözdizimine sahip, öğrenmesi oldukça kolay, modülerliği, okunabilirliği destekleyen, platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir."
harf = "a"
sayac = 0
for i in yazi:
    if i == harf:
        sayac += 1
print("Cümle içerisinde geçen a harfi sayısı :",sayac)
#----------------------------------------------------------#
print()
print()
#----------------------------------------------------------#
yazi = "Python üst düzey basit sözdizimine sahip, öğrenmesi oldukça kolay, modülerliği, okunabilirliği destekleyen, platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir."
sesli = "aeiıuüoö"
for i in yazi:
    if i in sesli:
        print(i,end=",")
#----------------------------------------------------------#
print()
print()
#----------------------------------------------------------#
yazi = "Python üst düzey basit sözdizimine sahip, öğrenmesi oldukça kolay, modülerliği, okunabilirliği destekleyen, platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir."
kelime = " "
sayac = 1
for i in yazi:
    if i in kelime:
        sayac += 1
print("Cümle içerisindeki kelime sayısı :",sayac)
#----------------------------------------------------------#
print()
print()
#----------------------------------------------------------#
yazi = "Python üst düzey basit sözdizimine sahip, öğrenmesi oldukça kolay, modülerliği, okunabilirliği destekleyen, platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir."
yazi2 = "Python interaktif yani etkileşimli bir programlama dilidir."
for i in yazi2:
    if not i in yazi:
        print(i,end=",")
print()
#----------------------------------------------------------#
print()
print()
#----------------------------------------------------------#
   






























































