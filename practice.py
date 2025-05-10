import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pensize(2)

hue = 0
for i in range(300):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.color(color)
    t.forward(i * 3)
    t.right(121)
    hue += 0.005 

turtle.done()
