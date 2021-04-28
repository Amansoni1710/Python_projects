from turtle import *
from random import randint
bgcolor("black")
h=1
speed(-1)
shape("turtle")
while h<400:
    r=randint(0,255)
    g=randint(0,255)
    s=randint(0,255)
    colormode(255)
    pencolor(r,g,s)
    forward(5+h)
    right(50.0)
    h=h+1
