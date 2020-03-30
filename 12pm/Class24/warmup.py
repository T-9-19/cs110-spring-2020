"""
File: warmup.py
Date: 3/30/20
Draw 4 circles and an equiangular diamond.
"""

import turtle

#class is turtle.Turtle, ted is an object,
#an instance of turtle.Turtle
ted = turtle.Turtle()

for side in range(4):
    ted.right(45)   #right is a method of turtle.Turtle class
    ted.forward(50) #forward is a method
    ted.right(45)

#pencolor is a method
#pencolor is an attribute of turtle.Turtle
#other methods and attributes:
#penwidth
#heading
#up/down
#position
#shape

for i in range(4):
    ted.circle(10 + i*10) #circle is a method

turtle.mainloop()
