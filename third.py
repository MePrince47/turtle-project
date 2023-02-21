import turtle as t
import random
t.bgcolor("black")

all_color = ["red","blue","white"]
t.speed("fastest")
for i in range(10):
    for i in range(4):
          t.pu()
          t.goto(0,0)
          t.pd()
          t.color(random.choice(all_color))
          t.pensize(1)
          t.circle(90,steps=19)
          t.right(100)
t.speed("fastest")
t.done()