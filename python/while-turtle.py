import turtle
clr_arr = ["red","green","blue"]
t = turtle.Turtle()
t.speed(0)
i=0

while i<100:
  i+=1
  print(i)
  t.forward(i)
  t.right(i+90)
  t.right(i*-1)
  t.setposition(i,i)


