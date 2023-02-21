import turtle as t
import random
t.bgcolor("black")

all_color = ["blue","white","red"]
t.speed(0)
for i in range(10):
    for i in range(4):
          t.pu()
          t.goto(0,0)
          t.pd()
          t.color(random.choice(all_color))
          t.pensize(3)
          t.circle(100,steps=15)
          t.right(100)

t.done()