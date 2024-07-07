from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Roboto', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.ht()
        self.setposition(0, 260)
        self.write("Score: " + str(self.score), False, align=ALIGNMENT, font=FONT)
        
    def refresh(self):
        self.clear()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.refresh()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        #print("self.score")