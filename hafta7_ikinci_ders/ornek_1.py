def puanHesaplama(vizePuanı, finalPuanı, vizeYuzdesi, finalYuzdesi):
    a = "Geçti - "
    if finalPuanı < 50:
        a = "Kaldı - "
    a += str(vizePuanı*vizeYuzdesi/100+finalPuanı*finalYuzdesi/100)
    return a

print(puanHesaplama(30,50,30,70))
#--------------------------------------------------------------------------#
print()
print()
#--------------------------------------------------------------------------#
def tekSayiBul(sayiListe):
    toplam = 0
    for i in sayiListe:
        if i % 2 == 1:
            toplam += i
    return toplam

print("Tek sayılar toplamı :",tekSayiBul([1,2,3,4,5,6,7,8,11,1773,1679]))
#--------------------------------------------------------------------------#
print()
print()
#--------------------------------------------------------------------------#
def tekSayiBul(sayiListe):
    toplam = 0
    for i in sayiListe:
        if i % 2 == 1:
            toplam += i
    return toplam

liste1 = []
while True:
    a = input("Listeye eklenecek sayıyı giriniz bitirmek için (x) yazınız : ")
    if a == "x":
        break
    liste1.append(int(a))
print("Tek sayiların toplamı :",tekSayiBul(liste1))
#--------------------------------------------------------------------------#
print()
print()
#--------------------------------------------------------------------------#
































    




