"""
THIS PROGRAM EXPERIEMENTS WITH GENERATIVE ART USING PYTHON TURTLE GRAPHICS
Educational source: https://spin.atomicobject.com/2021/12/14/generative-art-zero-random/
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

# Contains all steps for drawing anything on Turtle grid
def draw_line(row, col):
    lower_left = (
        (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )

    upper_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )

    lower_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )

    upper_left = (
        (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )

    res = random.randint(0, 1)  # Implementing randomness to change output every time

    if res == 0:    # 50% chance of getting 0
        t.goto(upper_left)
        t.pendown()
        t.goto(lower_right)
        t.penup()

    else:           # 50% chance of getting 1
        t.goto(lower_left)
        t.pendown()
        t.goto(upper_right)
        t.penup()

for row in range(DENSITY):
    for col in range(DENSITY):
        theColor = random.choice(colors)
        t.color(theColor)
        draw_line(row, col)

turtle.Screen().exitonclick()   # Keeps Turtle window open until user clicks anywhere
        
