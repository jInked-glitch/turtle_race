def winner_judge(self):
    winners = list(set(self.winners))
    self.message_turtle = Turtle()
    self.message_turtle.penup()
    self.message_turtle.hideturtle()
    self.message_turtle.goto(0, 0)

    # 表示するメッセージと色を事前に用意
    if self.user_bet in winners:
        self.message_turtle.color(self.user_bet)
        if len(winners) == 1:
            message = f"You've won! \nThe {self.user_bet} turtle is the winner!"
        else:
            message = f"It's a tie! \nYou bet on one of the winners: {self.user_bet}.\nWinning turtles: {', '.join(winners)}"
        sound = "yeah.wav"
    else:
        self.message_turtle.color("black")
        message = f"You've lost.\nWinning turtle(s): {', '.join(winners)}"
        sound = "lost.wav"

    # メッセージとサウンドを一括で実行
    self.message_turtle.write(message, align="center", font=("Courier", 16, "normal"))
    winsound.PlaySound(sound, winsound.SND_FILENAME)

✅ メリット
項目	改善内容
可読性	ロジックが「勝ち／同着／負け」で明確に分かれる
再利用性	message も sound も変数化されていて他で使える
保守性	フォントや write() の書き方を1箇所で管理できる
