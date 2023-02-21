import turtle as t
import random

def remote_tagent(circle,color,dis_range,radius):
	circle.speed(0)
	circle.color(color)
	for i in range(dis_range):
		circle.circle(radius*i)

remote_circle = t.Turtle()
remote_circle_screen =t.Screen()
remote_circle_screen.bgcolor("black")

remote_circle.width(1)
remote_circle.width(0)

all_color = ['yellow','red','pink']

for j in range(5):
	color = random.choice(all_color)
	for i in range(5):
		remote_tagent(remote_circle,color,10,(10+j))
		remote_circle.right(360/5)

remote_circle.width(3)
remote_circle.width(2)

remote_circle.penup()
remote_circle.home()
remote_circle.pendown()
t.done()


