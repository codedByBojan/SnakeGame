from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """A class to represent the score display in the Snake game."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        """ Update the displayed score on the game screen."""
        self.write(f"Score: {self.score}", 
            align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        """Ends the game and displays the outcome."""
        self.goto(0, 0)
        self.write(f"GAME OVER", 
            align=ALIGNMENT, font=FONT)
        
        
    def increase_score(self):
        """ Increase the current score and update the scoreboard."""
        self.score += 1
        self.clear()
        self.update_scoreboard()
