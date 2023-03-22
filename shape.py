

import turtle

t = turtle.Turtle()

t.speed(0)

i = 0

def shape():
  t.forward(100)
  t.right(25)
  t.forward(100)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(100)
  t.right(5)  
  t.forward(25)
  t.right(90)
  t.forward(25)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(50)
  t.right(45)
  t.forward(50)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(50)

while i<100:
  shape()
  t.left(10)
  t.forward(100)
  



  
