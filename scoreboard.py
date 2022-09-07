from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.level = 0
        self.numeric_data = ""
        self.name_data = ""
        with open("data.txt", mode="r") as record:
            self.data = record.read()
        for num in range(3):
            self.name_data += self.data[num]
        for num in range(len(self.data) - 4):
            self.numeric_data += self.data[num + 4]
        self.high_score = int(self.numeric_data)
        self.score()

    def score(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}            High Score: {self.name_data} {self.high_score}",
                   move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)

    def update_record(self):
        self.high_score = self.level
        with open("data.txt", mode="w") as record:
            record.write(f"{self.name_data} {str(self.high_score)}")
