# Functions that draw figures with the turtle module (the default turtle is used).
import turtle


def draw_square(length):
    # a square has 4 sides, after each side the turtle turns right by 90 degrees
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)


def draw_triangle(length):
    # an equilateral triangle (it is also isosceles): 3 sides, turn by 120 degrees
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)


def draw_rectangle(length_a, length_b):
    # a rectangle has two sides a and two sides b
    for i in range(2):
        turtle.forward(length_a)
        turtle.right(90)
        turtle.forward(length_b)
        turtle.right(90)
