liste = [1,2,3,4,5,"ankara"]
print(liste)
liste[0] = str("kocaeli")
liste[2] = float(1.5)
liste[5] = int(56)
print(liste)



print() #cümleyi harflere ayırma
meyve = "elma"
liste = list(meyve)
print(liste)



print() #sayı listesi oluşturma
liste = list(range(1,15,2))
print(liste)
liste.reverse()
print(liste)
liste.sort()
print(liste)



print() #cümleleri ayırma
bilgi = input("Lütfen bilgilerinizi araya virgül koyarak yazınız: ")
liste = bilgi.split(",")
print(liste)



print() #kelime sayma
metin = "23 Nisan herkese mutlu olsun"
kelimeler = metin.split(" ")
print("cümlenizde",len(kelimeler),"adet kelime vardır.")
