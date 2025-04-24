from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.count}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.count += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
