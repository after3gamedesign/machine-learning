import turtle
import random

t = turtle.Turtle()

t.shape('turtle')

i = 100
r = random.randint(0,i)

def path(i):
  n=0
  while n<20:
    t.forward(i)
    t.right(i)
    print(n)
    n+=1
  
path(i)
path(200)
path(r)
