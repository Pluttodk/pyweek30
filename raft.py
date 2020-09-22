import pygame as pg
import variables

class Raft:
    color = (102,51,0)
    
    def __init__(self):
        self.pieces = 0
        variables.RAFT_PIECES = 0
        self.x, self.y = variables.RAFT_LOCATION
        self.width = variables.RAFT_WIDTH
        self.height = variables.RAFT_HEIGHT
    def work(self):
        self.pieces += 1
        variables.RAFT_PIECES = self.pieces

    def draw(self, screen):
        for i in range(self.pieces):
            x = self.x + (variables.RAFT_WIDTH+variables.RAFT_SPACING)*i
            pg.draw.rect(screen, self.color, (x, self.y, self.width, self.height))
        
    def can_sail(self, criteria):
        return self.pieces >= criteria
    
    def calc_nearest_object(self, x):
        diff = abs(x-self.x)
        if diff <= variables.RANGE and self.pieces > 0:
            return self
        else:
            return None