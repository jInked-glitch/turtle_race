from turtle import Screen

is_race_on = False
screen = Screen()
screen.title("My Turtle race 🐢")
screen.setup(width=500, height=400)

from racing_turtle import RacingTurtle

while True:
    racing = RacingTurtle()
    racing.get_user_bet()
    racing.create_turtle()
    racing.start_animation()

    finish_line = 230
    winners = []

    while not racing.winners:
        racing.move_turtles()

    racing.winner_judge()

    racing.clear_turtle_message()

    user_answer = input("Do you want to play again? if yes input 'y', if not input 'n'").lower()
    if user_answer != "y":
        print("bye!")
        break

racing.screen.exitonclick()
