from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')
FONT_2 = ('Courier', 10, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f'Score:{self.score} ', align=ALIGNMENT, font=FONT)

    def coli_with_wall(self):
        self.goto(0, 0)
        self.write(f'GAME OVER ', align=ALIGNMENT, font=FONT)

    def restart_game_promt(self):
        self.goto(0, -20)
        self.write('Click on screen to restart', align='center', font=FONT_2)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
