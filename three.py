import turtle as t5
import random

t5.speed("fastest")
t5.bgcolor("black")
all_color = ["red","blue","white"]
for i in range(5):
    for i in range(4):
          t5.pu()
          t5.goto(00,0)
          t5.pd()
          t5.color(random.choice(all_color))
          t5.pensize(3)
          t5.circle(90,steps=4)
          t5.right(100)

t5.speed("fastest")

t5.done()