import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(1000)
import math

def msqu(iRange):
    length=2
    angle=5
    for i in range(iRange):
      t.forward(length)
      t.left(90)
      t.forward(length)
      t.left(90)
      t.forward(length)
      t.left(90)
      t.forward(length)
      t.length(angle)

 
        

msqu(100)

turtle.done()