import turtle as t 
import random

t.bgcolor("black")
all_color=["red","blue","white"]
t.speed(0)

for i in range(6):
	for i in range(4):
		t.pu()
		t.goto(0,0)
		t.pd()
		t.color(random.choice(all_color))
		t.pensize(3)
		t.circle(100,steps=6)
		t.right(100)

t.done()