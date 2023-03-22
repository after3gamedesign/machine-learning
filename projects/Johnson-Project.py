import turtle
#clcoding
t = turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.width(55)
t.speed(25)
col=("red","cyan","lime","yellow","pink","white","magenta")
for i in range(3100):
  t.pencolor(col[i%7])
  t.forward(i*3)
  t.right(121)
  
