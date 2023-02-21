import turtle as t
import random
t.bgcolor("black")

all_color = ["blue","white","red"]
t.speed(0)
for i in range (20):
    for i in range (2):
        t.pensize(2)
        t.goto(0,0)
        t.color("orange")
        t.forward(100)
        t.circle(50,steps=35)
        t.right(70)
        t.color("yellow")
        t.forward(50)
        t.right(120)
    t.left(30)

t.done()