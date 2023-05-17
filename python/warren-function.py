
import turtle
t = turtle.Turtle()
question = input("""What shape do you want?
A square,tringle,or pentagon?""")

question_2 = input("What color?")

question_3 = input("Width?(number)")

def square():
  import turtle
  i = 0
  t = turtle.Turtle()
  t.color(question_2)
  t.width(question_3)
  t.speed(0)
  while i<3:
	  t.forward(100)
  	t.left(90)
    
def tringle():
  import turtle
  i = 0
  t = turtle.Turtle()
  t.color(question_2)
  t.width(question_3)
  t.speed(0)
  while i<3:
	  t.forward(100)
  	t.left(120)
      
def pentagon():
  import turtle
  i = 0
  t = turtle.Turtle()
  t.color(question_2)
  t.width(question_3)
  t.speed(0)
  while i<3:
	  t.forward(100)
  	t.left(72)

if question == "square":
	square()
if question == "Square":
	square()

if question == "tringle":
	tringle()
if question == "tringle":
	tringle()
  
if question == "pentagon":
	tringle()
if question == "Pentagon":
	tringle()
  
else:
  s = input("You did not say a shape")
