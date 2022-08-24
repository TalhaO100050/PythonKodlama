import turtle
kalem = turtle.Turtle()
kalem.shape("turtle")

def kareciz(x,y):
    kalem.goto(x,y)
    kalem.forward(50)
    kalem.right(90)
    kalem.forward(50)
    kalem.right(180)
    for i in range(4):
        for i in range(10):
            kalem.dot()
            kalem.forward(10)
        kalem.left(90)

kalem.up()
kalem.goto(340,0)
kalem.down()
kalem.goto(-340,0)
kalem.up()
kalem.goto(0,340)
kalem.down()
kalem.goto(0,-340)
kalem.up()

kareciz(0,-200)
kareciz(-200,0)
kareciz(0,200)
kareciz(200,0)

turtle.done()
