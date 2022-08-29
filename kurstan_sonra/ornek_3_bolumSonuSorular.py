#Soru 1
demet1 = ("Ömer","Talha","Murat","Fatma","Hüseyin")
demet2 = ("Merhaba","Ben","Talha","Şu","An","Köydeyiz")
demet3 = demet1 + demet2
print(demet3.index(demet3[-1])+1)
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
#Soru 2
sayilar = (20,24,25,79,40,39,50)
for i in sayilar:
    if i % 5 == 0:
        print(i)
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
#Soru 3
demet = ("hasan","ali","c","mehmet","deniz","f","fatma")
yenidemet = demet[3:5]
print(yenidemet)
#("mehmet","deniz")
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
#Soru 4
Uygulama = ("ali","veli","ayşe","Fatma","Hayriye","ali","deniz")
print(Uygulama.count("ali"))
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
#Soru 5
sozluk = {'renk': 'mavi', 'kıyafet': 'pantolon', 'beden': 'M'}
for anahtar in sozluk:
    print(anahtar)
#renk
#kıyafet
#beden
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
#Soru 6
sozluk = {'renk': 'mavi', 'kıyafet': 'pantolon', 'beden': 'M'}
for anahtar in sozluk:
    print(anahtar,sozluk[anahtar])
    sozluk_bilesenleri=sozluk.items()
for bilesen in sozluk_bilesenleri :
    print(bilesen)
print(type(bilesen))# demet veri tipinde oluyor
#renk mavi
#kıyafet pantolon
#beden M
#("renk","mavi")
#("kıayfet","pantolon")
#("beden",M)
#string


