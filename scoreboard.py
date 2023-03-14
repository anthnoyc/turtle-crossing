from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.level_number = 0
        self.write(f"Level={self.level_number}", align="center", font=FONT)

    def level_up(self):
        self.level_number += 1
        self.clear()
        self.write(f"Level={self.level_number}", align="center", font=FONT)

    def end_game(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)