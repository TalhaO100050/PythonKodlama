liste = [1,2,3,4,5,6,7,8,9,10]
print(liste)
#1. Eleman
print(liste[0])
#6. Eleman
print(liste[5])
#Baştan 5. indise kadar
print(liste[:5])
#1. indisten 5. indise kadar
print(liste[1:7])
print(liste[5:])
print(liste[::2])

print(liste[6:9])
print(liste[6:])
print(liste[:6])
#2. eleman + | 6. eleman -
print(liste[1:5])
print(liste[4:])

print(liste[::-2])
print(liste[::-1])
print(liste[8::-1])

print() #append - ekleme
takimlar = ["gs","fb","bjk"]
takimlar.append("ts")
print(takimlar)

print() #insert - seçtiğimiz yere ekleme
sebzeler = ["lahana","marul","pırasa","ıspanak","fasulye"]
sebzeler.insert(2,"patlıcan")
print(sebzeler)

print() #copy - kopyalama
iller1 = ["konya","karaman","kocaeli","kayseri","kahramanmaraş"]
iller2 = ["sakarya"]
iller2 = iller1.copy()
print(iller2)

print() #count - sayma
takimlar = ["GS","FB","BJK","TS"]
print(takimlar.count("FB"))

print() #extend - ekleme
kus1 = ["bıldırcın","papağan","kartal","akbaba","şahin"]
kus2 = ["baykuş","muhabbet"]
kus1.extend(kus2)
print(kus1)

print() #index - yer belirleme
sebzeler = ["lahana","marul","prasa","ıspanak","fasulye"]
print(sebzeler.index("ıspanak"))

print() #clear - temizle
liste = ["nar","ayva","kiraz","kayısı","üzüm"]
liste.clear()
print(liste)

print() #pop - seçili değeri silme
sebzeler = ["lahana","marul","prasa","ıspanak","fasulye"]
sebzeler.pop(2)
print(sebzeler)

print() #remove - seçili değeri silme
sehirler = ["adana","ağrı","bursa","konya","ankara"]
sehirler.remove("konya")
print(sehirler)

print() #reverse - listeyi tersine çevirir
sayilar = [10,20,30,40,50,60,70]
sayilar.reverse()
print(sayilar)

print() #sort - alfabetik sıraya sıralama
isimler = ["elif","ayşe","kaan","hafsa"]
isimler.sort()
print(isimler)

print() #del - listeyi siler
takimlar = ["GS","FB","BJK","TS"]
del takimlar[2]
print(takimlar)
del takimlar





print() #len()
a = "Galatasaray"
print(len(a))

print()

takimlar = ["GS","FB","BJK","TS"]
print(len(takimlar))



print() #iç içe listeler
liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = [7,8,9]
yeniListe = [liste1,liste2,liste3]
print(yeniListe)

print()

sebzeler = [["yeşil","ıspanak"],["beyaz","lahana"],["turuncu","havuç"]]
print(sebzeler[2][1])

print()

birinciListe = [1,2,3]
ikinciListe = ["a","b","c"]
ucuncuListe = [40,50,60]
sonListe = [birinciListe,ikinciListe,ucuncuListe]
print(sonListe[1][0],sonListe[2][1])









