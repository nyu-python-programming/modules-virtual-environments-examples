# see https://docs.python.org/3/library/turtle.html
import turtle
import random

t = turtle.Turtle() # create a turtle
window = turtle.Screen() # create a window

# infinite loop!
while True:
    linelen = random.randint(0, 10)
    direction = random.randint(0, 1)
    rotation = random.randint(0, 360)

    t.forward(linelen)
    if direction == 0:
        t.right(rotation)
    else:
        t.left(rotation)

window.exitonclick() # exit when the user clicks
