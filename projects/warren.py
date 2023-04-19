class my_class:  
   class_1 = "\033[31mok press the output"
   class_2 = "Bad drawing"
   class_3 = "Good drawing"
   class_4 = "it is done"
   color = 'red'
   question_1 = "\033[31mwho made this project(upercase first)wait is Bob there because Bob made this project oops:"
   question_2 = "\033[31mwait.do you want the good drawing or the bad drawing(upercase first):"
   wrong = """WHO ON EARTH ARE YOU  
START OVER!!!
PRESS THE RUN BUTTON!!!"""
   nice_wrong = "start over(press the run the run button again)"
   number_1 = 100  
   number_2 = 90  
#see how many classes there are (11)!!!!!!!  
myname = input(my_class.question_1)
if myname == "Bob":
 print("\033[31mWelcome Bob")
 print("\033[31monly Bob can see me draw")
 q2 = input(my_class.question_2)
 import turtle
 t = turtle.Turtle()
 t.color(my_class.color)  
 t.speed(0)
 n3 = 4
 n4 = 60
 if q2 == my_class.class_2:
   print(my_class.class_1 ,"don't care about the thing below it will take a min")
   i = 0
   while i<n4:
     t.color(my_class.color)
     t.forward(my_class.number_1)
     t.left(my_class.number_2)
     i += 1
   print(my_class.class_4)
 if q2 == my_class.class_3:
   print(my_class.class_1)
   i = 0
   while i<n4:
     t.forward(my_class.number_1)
     t.left(my_class.number_2)
     t.forward(my_class.number_1)
     t.left(20)
     i += 1  
   print(my_class.class_4)  
 else:
   print(my_class.nice_wrong)
else:
  print(my_class.wrong ,
       """
\    /
 \  /
. \/ . {WHY DID YOU SNEAK INTO ME MY ARMY OF ANGRY FACES IS GOING TO ATTACK YOU!!!

______

\    /
 \  /              
  \/                            \        /
.    .{GET HIM/HER/THEY!!! ___   \      /   ___
                          |   |   \    /   |   |
______                    |___|    \  /    |___|
                                    \/            {HEY DONT MAKE ME GROW!!!

\    /                      |-----------------|
 \  /                                  
. \/ .{GET HIM/HER/THEY    

______       """)
