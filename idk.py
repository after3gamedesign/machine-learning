

import turtle

t = turtle.Turtle()
t.speed(0)
q=1
w=1
i=1
t.penup()
t.goto(-150,-25)
while i < 13:
  t.pendown()
  t.color('aquamarine')
  t.forward(40)
  t.right(30)
  i+=1
t.penup()
t.goto(-90,150)
while q < 4:
  t.pendown()
  t.color('magenta')
  t.forward(150)
  t.right(120)
  q+=1
t.penup()
t.goto(100,-5)
while w < 19:
  t.pendown()
  t.color('blue')
  t.forward(30)
  t.right(20)
  w+=1
  t.penup()
