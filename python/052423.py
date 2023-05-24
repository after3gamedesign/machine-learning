import turtle
import random

t = turtle.Turtle()
t.shape('turtle')

i=25
r=random.randint(0,i)
rint= random.randrange(25)

def path(r,rint):
  while i > 0:
    t.forward(r)
    t.right(r)
    t.forward(i)
    t.right(i)
 
path(r,rint)
