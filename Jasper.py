import turtle

for x in range(4):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    
turtle.done()

Microsoft Windows [Version 10.0.18363.1082]
(c) 2019 Microsoft Corporation. Alle rechten voorbehouden.

C:\Users\Jasper>color 2

C:\Users\Jasper>py
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import turtle
>>> turtle.setup(400, 400, 0, 0)
>>> turtle.color("blue")
>>> turtle.forward(100)
>>> turtle.right(45)
>>> turtle.forward(100)
>>> turtle.right(45)
>>> venster = turtle.getscreen()
>>> venster.bgcolor("yellow")
>>> turtle.reset()
>>> turtle.bgcolor("black")
>>> turtle.pencolor("#FFFFFF")
>>> turtle.fillcolor("#FF0000")
>>> turtle.begin_fill()
>>> turtle.forward(100)
>>> turtle.right(120)
>>> turtle.forward(100)
>>> turtle.right(120)
>>> turtle.forward(100)
>>> turtle.end_fill()
