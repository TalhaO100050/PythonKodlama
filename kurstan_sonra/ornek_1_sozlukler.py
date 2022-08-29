sozluk1 = {1:"Merhaba","2.":"help"}
print(sozluk1)
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
print(sozluk1.keys())
print(sozluk1.values())
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
kisi = {"Ad":"Talha","Soy Ad":"Kılıçarslan","Yaş": 15}
print(kisi)
print(kisi["Ad"])
print(kisi["Soy Ad"])
print(kisi["Yaş"])
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
kisi = {"Ad":"Talha","Soy Ad":"Bilinmiyor"}
print(kisi)
kisi["Soy Ad"] = "Kılıçarslan"
print(kisi)
kisi["Yaş"] = 15
print(kisi)
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
kisi = {"Ad":"Talha","Soy Ad":"Kılıçarslan","Yaş": 15,"Gereksiz Değer":"Değer"}
print(kisi)
kisi.pop("Gereksiz Değer")
print(kisi)
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
kisi = {
    "Ad":"Talha",
    "Soy Ad":"Kılıçarslan",
    "Yaş": 15
    }
print(kisi)
kisi.popitem()
print(kisi)
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
kisi = {"Ad":"Talha","Soy Ad":"Kılıçarslan","Yaş": 15,"Gereksiz Değer":"Değer"}
print(kisi)
del kisi["Gereksiz Değer"]
print(kisi)
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
kisi = {"Ad":"Talha","Soy Ad":"Kılıçarslan","Yaş": 15,"Gereksiz Değer":"Değer"}
print(kisi)
kisi.clear()
print(kisi)
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
kisi = {"Ad":"Talha","Soy Ad":"Kılıçarslan","Yaş": 15}
print(kisi)
del kisi
print("kisi sözlüğü silindi.")
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
sozluk = {"Ad":"Talha",1:[5,4]}
print(sozluk)
print(sozluk["Ad"])
print(sozluk[1])
print(sozluk.get(1))
print(sozluk[1][0])
#-----------------------------------------------------------#
print()
print()
#-----------------------------------------------------------#
sayilar = {"Sıfır":0,"Bir":1,"İki":2,"Üç":3}
print(sayilar)
print(sayilar["Bir"])
print(sayilar["Üç"])











