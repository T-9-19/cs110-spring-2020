"""
File: warmup.py
Date: 3/30/20
Draw 4 circles and an equiangular diamond.
"""

import turtle

alex = turtle.Turtle()

for index in range(4):
    alex.right(45)
    alex.forward(50)
    alex.right(45)

radius = 10
for index in range(4):
    alex.circle(radius)
    radius += 10

turtle.mainloop()
