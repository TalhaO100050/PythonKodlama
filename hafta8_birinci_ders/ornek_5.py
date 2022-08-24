import turtle
def ciz(sayi):
    kalem = turtle.Turtle()
    x = 360/sayi
    for i in range(sayi):
        kalem.forward(600/sayi)
        kalem.left(x)
    turtle.done()

b = input("Sayı giriniz : ")
ciz(int(b))
