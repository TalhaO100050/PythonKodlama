import turtle
def sekilciz(sekilKose,sekilSayi,renk):
    x = 360 / sekilKose
    kalem = turtle.Turtle()
    kalem.color(renk)
    for i in range(sekilSayi):
        for i in range(sekilKose):
            kalem.forward(80)
            kalem.left(x)
        kalem.left(360/sekilSayi)

x = int(input("Bir pozitif sayı giriniz: "))
y = int(input("Bir pozitif satı daha giriniz: "))
z = input("Renk kodu giriniz: ")
sekilciz(x,y,z)
