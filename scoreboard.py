from turtle import Turtle

MOVE = False
Alignment = "center"
Font = ("Courier", 25, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", move = MOVE, align = Alignment, font = Font)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=MOVE, align=Alignment, font=Font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()