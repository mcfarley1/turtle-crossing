import os
from turtle import Turtle
FONT = ("Courier", 16, "normal")

PROJ_DIRECTORY = os.path.dirname(__file__) # get the path to the current directory
HIGH_SCORE_FNAME = os.path.join(PROJ_DIRECTORY, "high_score.txt") # absolute path to high scores file

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.level = 0
        with open(HIGH_SCORE_FNAME, mode="r") as record:
            hs_data = record.read()
        self.high_score_name, high_score_str = hs_data.split()
        self.high_score = int(high_score_str)
        self.score()

    def score(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}            High Score: {self.high_score_name} {self.high_score}",
                   move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)

    def update_high_score(self):
        self.high_score = self.level
        with open(HIGH_SCORE_FNAME, mode="w") as record:
            record.write(f"{self.high_score_name} {self.high_score}")
