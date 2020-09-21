import pygame as pg

class Raft:
    color = (102,51,0)
    
    def __init__(self):
        self.pieces = 0
        self.x, self.y = 800,300
        self.width = 12
        self.height = 20
    
    def work(self):
        self.pieces += 1

    def draw(self, screen):
        for i in range(self.pieces):
            x = self.x + (10*i)
            pg.draw.rect(screen, self.color, (x, self.y, self.width, self.height))