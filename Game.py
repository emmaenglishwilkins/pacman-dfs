from Pacman import Pacman
from Ghost import Ghost

class Game: 
    def __init__(self, lvl): # constructor
        self.running = False # game is paused 
        self.level = lvl
        self.levels = [[350, 250], [150, 450], [150, 450], [0, 600]]
        self.lives = 3
        self.pacman = Pacman()
        self.ghosts = [Ghost(), Ghost(), Ghost(), Ghost()]
        self.gameover = False
        self.paused = True 




