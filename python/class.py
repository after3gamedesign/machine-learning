import turtle
t = turtle.Turtle()

def pattern():
  t.forward(100)
  t.right(85)
  t.forward(100)

class Shape:
  def __init__(self, posx, posy,  col, wid, patt):
    self.posx = posx
    self.posy = posy
    self.col = t.color(col)
    self.str = wid
    self.patt = patt
    t.goto(posx,posy)

shape_0 = Shape(0, 0, "green", t.width(5),t.forward(100))
shape_1 = Shape(-180, -180, "red", t.width(9),pattern())
             
