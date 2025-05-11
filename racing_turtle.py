from turtle import Screen, Turtle
import random
import time
import winsound

class RacingTurtle:
    def __init__(self):
        # 「クラスが持つべきデータ（属性）」を self. にまとめる
        self.message_turtle = None
        self.screen = Screen()
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.all_turtles =[]
        self.user_bet = None
        self.winners = []
        self.finish_line = 230

    def get_user_bet(self):
        self.user_bet = self.screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:  ")

    def create_turtle(self):
        y_position = -100
        for turtle_index in range(len(self.colors)):
            # for turtle_index in range(len(colors)) 
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(self.colors[turtle_index])
            new_turtle.penup()
            new_turtle.goto(x=-240, y=y_position + 30)
            y_position += 30
            self.all_turtles.append(new_turtle)

    def start_animation(self):
        start_animation = Turtle()
        start_animation.hideturtle()
        start_animation.penup()
        start_animation.goto(0, 0)
        start_animation.write("Ready...", align="center", font=("Courier", 16, "normal"))
        time.sleep(1)
        start_animation.clear()

        start_animation.write("Set...", align="center", font=("Courier", 16, "normal"))
        time.sleep(1)
        start_animation.clear()

        start_animation.write("Go!", align="center", font=("Courier", 16, "normal"))

        winsound.PlaySound("start.wav", winsound.SND_FILENAME)

        start_animation.clear()

    def move_turtles(self):
        for turtle in self.all_turtles:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
            if turtle.xcor() >= self.finish_line:
                if turtle.pencolor() not in self.winners:
                    self.winners.append(turtle.pencolor())

    def winner_judge(self):
        winners = list(set(self.winners))
        self.message_turtle = Turtle()
        self.message_turtle.penup()
        self.message_turtle.hideturtle()
        self.message_turtle.goto(0, 0)

        if self.user_bet in winners:
            if len(self.winners) == 1:
                self.message_turtle.color(self.user_bet)
                self.message_turtle.write(f"You've won! \nThe {self.user_bet} turtle is the winner!", align="center",
                                     font=("Courier", 16, "normal"))
                winsound.PlaySound("yeah.wav", winsound.SND_FILENAME)

            else:
                self.message_turtle.color(self.user_bet)
                self.message_turtle.write(
                    f"It's a tie! \nYou bet on one of the winners: {self.user_bet}.\nWinning turtles: {', '.join(winners)}",
                    align="center", font=("Courier", 16, "normal"))
                winsound.PlaySound("yeah.wav", winsound.SND_FILENAME)

        else:
            self.message_turtle.color("black")
            self.message_turtle.write(f"You've lost.\nWinning turtle(s): {', '.join(winners)}", align="center",
                                 font=("Courier", 16, "normal"))
            winsound.PlaySound("lost.wav", winsound.SND_FILENAME)

    def clear_turtle_message(self):
        if hasattr(self, "message_turtle"):
            self.message_turtle.clear()
        for turtle in self.all_turtles:
            turtle.hideturtle()  # ← カメの姿を消す！

        self.all_turtles = []  # ← カメリストもリセット（次のレース用）
        self.winners = []  # ← 勝者リストもリセット
