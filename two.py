import turtle as t
import random 

t.bgcolor("black")
all_color=["red","blue","yellow","white"]

t.pencolor(random.choice(all_color))
t.speed(0)
for i in range(50):
	t.pu()
	t.pencolor(random.choice(all_color))
	t.goto(0,0)
	t.pd()
	t.forward(150)
	t.left(123)

t.up()
t.goto(95,-170)
t.down()

t.speed(5)
t.color('red')
t.circle(200)
t.up()
t.down()
t.up()
t.goto(0,-180)
t.down()


t.done()