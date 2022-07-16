from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_highscore()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.h_score}", align = "center", font =('Arial', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def read_highscore(self):
        with open('highscore.txt') as file:
            self.h_score = int(file.read())

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align = "center", font =('Arial', 15, 'normal'))
        if self.score > self.h_score:
            with open('highscore.txt', 'w') as file:
                file.write(str(self.score))



