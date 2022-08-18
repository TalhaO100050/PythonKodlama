import turtle
sayac = 0
kalem = turtle.Turtle()
while not sayac == 360:
    kalem.forward(1)
    kalem.left(1)
    sayac += 1
sayac = 0
while not sayac == 240:
    kalem.forward(1)
    kalem.left(1.5)
    sayac += 1
sayac = 0
while not sayac == 180:
    kalem.forward(1)
    kalem.left(2)
    sayac += 1
sayac = 0
while not sayac == 90:
    kalem.forward(1)
    kalem.left(4)
    sayac += 1
sayac = 0
while not sayac == 45:
    kalem.forward(1)
    kalem.left(8)
    sayac += 1
kalem.left(90)
kalem.forward(300)

turtle.done()
