import turtle as t
t.bgcolor("black")
t.speed(0)

t.speed("fastest")
for i in range(10):
    for i in range(4):
          t.pu()
          t.goto(0,0)
          t.pd()
          t.color('white')
          t.pensize(1)
          t.circle(100,steps=15)
          t.right(100)
t.done()