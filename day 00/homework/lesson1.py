from turtle import *

#we want to paint a house

#step1: draw a square

speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square
#step2: draw a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(0, 140)
pendown()
color("brown")
left(120)
forward(60)
left(90)
forward(60)

penup()
goto(200, 140)
pendown()
left(90)
forward(60)
right(90)
forward(60)

penup()
goto(0, 170)
pendown()

color("black")
right(90)
forward(60)

penup()
goto(30, 170)
pendown()
left(90)
forward(30)
left(180)
forward(60)


penup()
goto(200, 170)
pendown()
right(90)
forward(60)
left(180)
forward(30)
left(90)
forward(30)
left(180)
forward(60)

penup()
goto(40, 270)
pendown()
color("purple")
begin_fill()
left(180)
forward(50)
right(90)
forward(30)
right(90)
end_fill()

penup()
goto(130, 60)
pendown()
right(90)
color("black")
forward(10)



exitonclick()







