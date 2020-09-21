import pygame as pg
from raft import Raft
class House:
    """
    The only place where Timmy can rest and where he can build the dock
    """

    def __init__(self):
        self.color_base = (100,100,100)
        self.color_roof = (0,200,0)
        self.x, self.y = (100, 400)
        self.width = 50
        self.height = 50
        self.raft = None
    
    def draw(self, screen):
        x1 = self.x
        x2 = self.x - self.width // 2
        x3 = self.x - self.width
        y1 = self.y - self.height
        y2 = int(self.y - self.height * 1.5)
        y3 = self.y - self.height
        #Draw roof
        pg.draw.rect(screen, self.color_base, (self.x-self.width, self.y-self.height, self.width, self.height))
        pg.draw.polygon(screen, self.color_roof, [[x1,y1],[x2,y2],[x3,y3]])
        if self.raft != None:
            self.raft.draw(screen)

    def work(self):
        self.color_base = (self.color_base[0]+1, self.color_base[1]+1, self.color_base[2]+1)

    def build_raft(self, ressources):
        if ressources > 10:
            if self.raft == None:
                self.raft = Raft()
            self.raft.work()
            return True
        else:
            print("You need to chop more trees")
            return False
    def get_pos(self):
        return (self.x, self.y)