import turtle as t
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as file:
                self.high_score = self.score
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

