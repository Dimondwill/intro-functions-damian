import turtle
from turtle import *
t = Turtle()


t.shape('turtle')

def rectangle(length, height):
    t.forward(length)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(height)
    t.left(90)
rectangle(100, 125)

turtle.clearscreen()

import turtle
from turtle import *
t = Turtle()


t.shape('turtle')

def triangle(four):
    t.forward(four)
    t.left(120)
    t.forward(four)
    t.left(120)    
    t.forward(four)
    t.left(120)    
triangle(90)
    
    
turtle.done()