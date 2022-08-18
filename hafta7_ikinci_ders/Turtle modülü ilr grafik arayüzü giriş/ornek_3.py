import turtle
def sekilCiz(sekil):
    if sekil == "üçgen":
        kalem = turtle.Turtle()
        kalem.forward(100)
        kalem.left(120)
        kalem.forward(100)
        kalem.left(120)
        kalem.forward(100)
    if sekil == "kare":
        kalem = turtle.Turtle()
        kalem.forward(100)
        kalem.left(90)
        kalem.forward(100)
        kalem.left(90)
        kalem.forward(100)
        kalem.left(90)
        kalem.forward(100)
    if sekil == "daire":
        sayac = 0
        kalem = turtle.Turtle()
        while not sayac == 360:
            kalem.forward(1)
            kalem.left(1)
            sayac += 1
    if sekil == "beşgen":
        kalem = turtle.Turtle()
        kalem.forward(100)
        kalem.left(72)
        kalem.forward(100)
        kalem.left(72)
        kalem.forward(100)
        kalem.left(72)
        kalem.forward(100)
        kalem.left(72)
        kalem.forward(100)
    if sekil == "altıgen":
        kalem = turtle.Turtle()
        kalem.forward(100)
        kalem.left(60)
        kalem.forward(100)
        kalem.left(60)
        kalem.forward(100)
        kalem.left(60)
        kalem.forward(100)
        kalem.left(60)
        kalem.forward(100)
        kalem.left(60)
        kalem.forward(100)
    if sekil == "sekizgen":
        kalem = turtle.Turtle()
        kalem.forward(100)
        kalem.left(45)
        kalem.forward(100)
        kalem.left(45)
        kalem.forward(100)
        kalem.left(45)
        kalem.forward(100)
        kalem.left(45)
        kalem.forward(100)
        kalem.left(45)
        kalem.forward(100)
        kalem.left(45)
        kalem.forward(100)
        kalem.left(45)
        kalem.forward(100)

    turtle.done()

while True:
    a = input("Şekil adı giriniz (üçgen,kare,daire,beşgen,altıgen,sekizgen) : ")
    if not a == "üçgen" and not a == "kare" and not a == "daire" and not a == "beşgen" and not a == "altıgen" and not a == "sekizgen":
        print("Tekrar deneyizin.")
        continue
    print("Şekil çiziliyor...")
    sekilCiz(a)
    break
