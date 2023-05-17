import turtle

t = turtle.Turtle()

class Shape:
  def __init__(self, posx, posy,  col, str, mov):
    self.posx = posx
    self.posy = posy
    self.col = col
    self.str = str
    self.mov = mov

shape = Shape(0, 0, "green", t.width(5), t.forward(20))
shape = Shape(90, 90, "red", t.width(9), t.left(70))
