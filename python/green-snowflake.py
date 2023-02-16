import turtle


def tree(branchLen,t):
    if branchLen > 10:
        t.forward(branchLen)
        t.right(45)
        tree(branchLen-15,t)
        t.left(45)
        tree(branchLen-15,t)
        t.right(45)
        t.backward(branchLen)

def main():
    turtle.Screen().bgcolor("purple")
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(90)
    t.down()
    t.color("green")
    num = 20   
    while num < 100:
      print(num)
      tree(num,t)
      num = num + 1
    else:
      print("done")
    myWin.exitonclick()

main()
