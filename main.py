from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.title("My Turtle race 🐢")
screen.setup(width=500, height=400)

user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -100
all_turtles =[]


for turtle_index in range(len(colors)):
    # for turtle_index in range(len(colors)) ← 柔軟性が高くてベスト（数が変わっても安心）
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position +30)
    y_position += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on =  False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won: The {winning_color} turtle is the winner! ")
            else:
                print(f"You've lost: The {winning_color} turtle is the winner! ")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()