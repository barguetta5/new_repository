from turtle import Turtle ,Screen
import random


is_race = False
screen = Screen()
screen.setup(width=500,height=400)
screen.colormode(255)
answer = screen.textinput("hey","who do you think going to win")
is_race = True


color_list = ["red","pink","yellow","blue","black","grey"]
turtle_list = []


x = -200
y = -100
for i in range(6):
    turt = Turtle(shape="turtle")
    turt.penup()
    turt.color(color_list[i])
    turt.goto(x,y)
    turtle_list.append(turt)
    y+=30


if answer:
    is_race = turt

while is_race:
    for turtlle in turtle_list:
        if turtlle.xcor() >230:
            color_win = turtlle.pencolor()
            print(f"the winer is {color_win}, and you choose {answer}")
            is_race = False
            break

        turtlle.forward(random.randint(0,10))




screen.exitonclick()