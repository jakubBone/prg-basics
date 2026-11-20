# A program that draws a square using the function draw_square() from the module figures.py.
# (the task calls this file draw_figures.py)

import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

turtle.speed(5)

# Side length
side_length = 100

# Draw a square
figures.draw_square(side_length)

# Hide the turtle and finish
turtle.hideturtle()
window.mainloop()
