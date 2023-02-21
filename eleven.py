import turtle as t
t.bgcolor("black")
t.speed(0)
for i in range (10):
    for i in range (2):
        t.pensize(3)
        t.pu()
        t.goto(0,0)
        t.pd()
        t.color("red")
        t.begin_fill()
        t.forward(30)
        t.right(50)
        t.color("orange")
        t.forward(50)
        t.circle(5,steps=6)
        t.right(120)
        t.end_fill()
    t.right(100)

t.done()