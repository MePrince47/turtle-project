import turtle as t
import random
t.bgcolor("black")
t.speed(0)

for i in range (20):
	for i in range (4):
		t.pensize(3)
		t.goto(0,0)
		t.color("black")
		t.begin_fill()
		t.forward(30)
		t.right(50)
		t.color("orange")
		t.forward(50)
		t.circle(5,steps=6)
		t.right(120)
		t.end_fill()
	t.right(60)

t.done()