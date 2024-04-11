from turtle import *

color("red")
bgcolor("black")

speed(1)

def draw_heart():
    left(140)
    forward(180)
    circle(-90, 200)
    left(120)
    circle(-90, 200)
    forward(180)

draw_heart()
