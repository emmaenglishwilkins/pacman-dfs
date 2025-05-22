import random

class Ghost: 
    def __init__(self, row, col, color):
        self.row = row
        self.col  = col 
        self.color = color
        self.direction = random.randint(0, 3)
        self.speed = 0.25
        self.alive = True