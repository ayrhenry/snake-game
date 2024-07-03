from turtle import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_positions:
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(position)
    segments.append(turtle)
    

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)


    for seg_num in range(len(segments) - 1, 0, -1):
        segments[seg_num].forward(20)
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
        




screen.exitonclick()