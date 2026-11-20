# A program that draws each of the figures (square, triangle, rectangle) twice, in different locations.

import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

turtle.speed(5)


def go_to(x, y):
    # penup() lifts the pen, so the turtle moves without drawing; pendown() puts the pen down again
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


## Draw figures
go_to(-250, 100)
figures.draw_square(80)
go_to(100, 100)
figures.draw_square(50)

go_to(-250, -50)
figures.draw_triangle(80)
go_to(100, -50)
figures.draw_triangle(50)

go_to(-250, -200)
figures.draw_rectangle(120, 50)
go_to(100, -200)
figures.draw_rectangle(60, 30)

# Hide the turtle and finish
turtle.hideturtle()
window.mainloop()
