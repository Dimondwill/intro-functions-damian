import random

'''rannum = random.randint(1, 10)  # Generates an integer between 1 and 10 (inclusive)
inputnum = int(input("Guess a number between 1 and 10: "))
if inputnum == rannum:
    print("You guessed it right!")'''

import turtle
t = turtle.Turtle()
t.speed(100000000)
'''def msqu(iRange):
    length=5
    angle=5
    for i in range(iRange):
      t.forward(length)

@@ -16,11 +16,33 @@ def msqu(iRange):
      t.forward(length)
      t.left(90)
      t.forward(length)
      t.length(angle)
      t.left(90)
      t.right(angle)
      length += 5
msqu(60)'''

def mstar(irange):
    length=25
    angle=144
    for i in range(irange):
        t.forward(length)
        t.left(angle)
        t.forward(length)
        t.left(angle)
        t.forward(length)
        t.left(angle)
        t.forward(length)
        t.left(angle)
        t.forward(length)
        t.left(angle)
        t.right(5)
        length += 5
mstar(60)

turtle.done()
