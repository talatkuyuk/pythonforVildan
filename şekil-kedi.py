import turtle as t

def dortgen (horizontal,vertical,color):
    t.pendown()
    t.pensize(2)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed("fast")
t.bgcolor("light blue")
#bacaklar
t.goto(0,-50)
dortgen(15,100,"black")
t.goto(40,-50)
dortgen(15,100,"black")
t.goto(80,-50)
dortgen(15,100,"black")
t.goto(120,-50)
dortgen(15,100,"black")
#gövde
t.goto(-8,-30)
dortgen(150,80,"black")

