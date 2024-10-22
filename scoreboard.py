from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.score = 0
        self._update_scoreboard()

    def _update_scoreboard(self):
        """ Update the scoreboard. """
        self.clear()
        msg = f"Score: {self.score}"
        self.write(msg, move=False, align=ALIGNMENT, font=FONT)

    def display_game_over(self):
        """ Display game over message at the center of the screen. """
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """ Increase the score by value of 1. """
        self.score += 1
        self._update_scoreboard()
