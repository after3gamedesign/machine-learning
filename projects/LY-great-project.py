import turtle
#clcoding.com
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
s = turtle.Screen()
s.bgcolor("black")
t.width(15)
col = ("cyan","purple","lime","red","orange","yellow")
for i in range(3100):
  t.pencolor(col[i%6])
  t.circle(i*4)
  t.right(121)
