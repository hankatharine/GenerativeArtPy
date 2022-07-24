"""
This program aims to generate random integers that represent the grid
placement of randomly sized/coloured dots to create an interactive
piece of generative artwork

*Optional: add user input area where user can dictate generative-ness
"""

import turtle, random

CANVAS_SIZE = 500   # Width and height of canvas
DENSITY = 12        # How many rows/columns on grid

# Turtle Graphics setup initializations
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
s.setup(CANVAS_SIZE, CANVAS_SIZE)
t.width(12)
t.penup()
colors = ["#E464D5", "#C1F79B", "#C69BF7", "#FFC300"]


""" Draw dot size randomly depending on generative random number """
def draw_dot(row, col):
    t.goto(random.randint(-150,0),random.randint(0,150))
    t.pendown()
    turtle.dot(random.randint(0,100), color=colors[random.randint(0, len(colors)-1)])
    t.penup()

turtle.Screen().exitonclick()