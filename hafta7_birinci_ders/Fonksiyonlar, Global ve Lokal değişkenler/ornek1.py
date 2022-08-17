def sayiÇiftMi(sayi):
    if sayi % 2 == 0:
        print("Çift sayı")
    else:
        print("Tek sayı")
        
a = int(input("Sayı giriniz :"))
sayiÇiftMi(a)
#--------------------------------------------------#
def yaziYaz(text,number):
    if number < 1:
        print("Pozitif bir sayı giriniz.")
        a = input("Metin giriniz : ")
        b = int(input("Sayısını giriniz : "))
        yaziYaz(a,b)
    else:
        while number > 0:
            print(text)
            number -= 1

a = input("Metin giriniz : ")
b = int(input("Sayısını giriniz : "))
yaziYaz(a,b)
#--------------------------------------------------#
def asalMi(sayi):
    asal = 0
    if not sayi == 1:
        for i in range(2,sayi):
            if sayi % i == 0:
                asal = 1
                if i == 1 and i == sayi:
                    asal = 0
        if asal == 1:print("Bu sayı asal değildir.")
        else:print("Bu sayı asaldır.")
    else:print("Bu sayı asal değildir.")    

a = int(input("Sayı giriniz : "))
asalMi(a)
#--------------------------------------------------#
def faktoriyel(sayi):
    x = 1
    for i in range(1,sayi+1):
        x = x * i
    print(x)

a = int(input("Sayı giriniz : "))
faktoriyel(a)












