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
        self.screen = screen
        for i in range(0,self.pieces,4):
            vertical = i%2
            stop = 4 if i+4 <= self.pieces else self.pieces
            for j in range(stop):
                x = self.x + (variables.RAFT_WIDTH+variables.RAFT_SPACING)*j
                if not vertical:
                    pg.draw.rect(screen, self.color, (x, self.y, self.width, self.height))
                else:
                    pg.draw.rect(screen, self.color, (x, self.y, self.height, self.width))
        
    def can_sail(self, criteria):
        return self.pieces >= criteria
    
    def calc_nearest_object(self, x):
        diff = abs(x-(self.x+(self.pieces*self.width)))
        diff2 = abs(x-self.x)
        if (diff <= variables.RANGE or diff2 <= variables.RANGE) and self.pieces > 0:
            return self
        else:
            return None
    
    def sail(self, user_movement, island):
        for i in range(100):
            start_x = self.x + (i*3)
            island.draw(is_sailing=True)
            for i in range(self.pieces):
                x = start_x + (variables.RAFT_WIDTH+variables.RAFT_SPACING)*i
                pg.draw.rect(self.screen, self.color, (x, self.y, self.width, self.height))
            user_movement(self.screen, start_x+(2*self.width))
            pg.time.delay(10)
            pg.display.flip()
        variables.LEVEL += 1