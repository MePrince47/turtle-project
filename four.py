import turtle as t

t.bgcolor("black")

t.speed("fastest")
for i in range (10):
    for i in range (2):
        t.pensize(5)
        t.goto(0,0)
        t.color("white")
        t.forward(100)
        t.right(60)
        t.color("red")
        t.forward(50)
        t.right(120)
    t.right(30)
t.done()