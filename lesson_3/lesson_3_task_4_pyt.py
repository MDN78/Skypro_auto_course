from turtle import *
import math

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(800, 800)

pd()
fd(25)

circle(100, 90)
circle(120, 90)
fd(10)

circle(120, 90)
circle(100, 90)

fd(25)

pu()
goto(60, 100)
begin_fill()
circle(18)
end_fill()

pu()
goto(-60, 100)
begin_fill()
circle(18)
end_fill()

pu()
my_turtle.goto(0, 0)
a = 70
b = 15
dx = my_turtle.xcor()
dy = my_turtle.ycor()
for deg in range(361):
    rad = math.radians(deg)
    x = a * math.sin(rad) + dx
    y = -b * math.cos(rad) + b + dy
    my_turtle.goto(x, y)



my_turtle.up()
my_turtle.goto(0, -100)
my_turtle.write("Питон Николай", move=False, align="center", font = ("Arial", 34, "bold"))


# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()