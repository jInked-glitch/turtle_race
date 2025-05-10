from turtle import Turtle, Screen
import random
import time
import winsound

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
    start_turtle = Turtle()
    start_turtle.hideturtle()
    start_turtle.penup()
    start_turtle.goto(0, 0)
    start_turtle.write("Ready...", align="center", font=("Courier", 16, "normal"))
    time.sleep(1)
    start_turtle.clear()

    start_turtle.write("Set...", align="center", font=("Courier", 16, "normal"))
    time.sleep(1)
    start_turtle.clear()

    start_turtle.write("Go!", align="center", font=("Courier", 16, "normal"))

    winsound.PlaySound("start.wav", winsound.SND_FILENAME)

    # time.sleep(0.5)
    start_turtle.clear()

is_race_on = True
finish_line = 230
winners = []

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() >= finish_line:
            winners.append(turtle.pencolor())
            is_race_on = False  # 一旦止める（必要に応じて条件を工夫）

# 同着も考慮した勝敗判定
winners = list(set(winners))
message_turtle = Turtle()
message_turtle.penup()
message_turtle.goto(0, 0)

if user_bet in winners:
    if len(winners) == 1:
        message_turtle.color(user_bet)
        message_turtle.write(f"You've won! \nThe {user_bet} turtle is the winner!", align = "center", font =("Courier", 16, "normal"))
        winsound.PlaySound("yeah.wav", winsound.SND_FILENAME)
    else:
        message_turtle.color(user_bet)
        message_turtle.write(f"It's a tie! \nYou bet on one of the winners: {user_bet}.\nWinning turtles: {', '.join(winners)}", align = "center", font =("Courier", 16, "normal"))
        winsound.PlaySound("yeah.wav", winsound.SND_FILENAME)
else:
    message_turtle.color("black")
    message_turtle.write(f"You've lost.\nWinning turtle(s): {', '.join(winners)}", align = "center", font =("Courier", 16, "normal"))
    winsound.PlaySound("lost.wav", winsound.SND_FILENAME)

screen.exitonclick()
