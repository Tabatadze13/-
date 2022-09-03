from turtle import *

#We want to paint a house

#step 1: draw a square

begin_fill()
speed(30)
width(7)
color("grey")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
color("black")
begin_fill()
penup()
goto(25, 0)
pendown()
left(90)
forward(90)
right(90)
forward(50)
right(90)
forward(90)
end_fill()

#end of door

#begin of window
color("black")
begin_fill()
penup()
goto(110, 40)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#end of window

#start of roof



penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of roof






exitonclick()