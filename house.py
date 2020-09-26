import pygame as pg
from raft import Raft
import variables
class House:
    """
    The only place where Timmy can rest and where he can build the dock
    """

    def __init__(self):
        self.color_base = (100,100,100)
        self.color_roof = (0,200,0)
        self.x, self.y = variables.HOUSE_CENTER
        self.width = 50
        self.height = 50
        self.raft = None
        self.life = 0
        self.house_sprite = pg.image.load("sprites/house.png")
    
    def draw(self, screen, is_sailing=False):

        #Draw roof
        screen.blit(self.house_sprite, (self.x, self.y))
        
        if self.raft != None and not is_sailing:
            self.raft.draw(screen)

    def work(self):
        self.color_base = (self.color_base[0]+1, self.color_base[1]+1, self.color_base[2]+1)

    def is_dead(self):
        return False

    def build_raft(self, ressources):
        if ressources >= variables.RAFT_COST:
            if self.raft == None:
                self.raft = Raft()
            self.raft.work()
            return True
        else:
            print("You need to chop more trees")
            return False
    def get_pos(self):
        return (self.x+self.house_sprite.get_rect().width//2, self.y+self.house_sprite.get_rect().height//2)
    
    def calc_nearest_object(self, x):
        if self.x-variables.RANGE <= x <= (self.x+self.house_sprite.get_rect().width)+variables.RANGE:
            return self
        elif self.raft != None:
            return self.raft.calc_nearest_object(x)
        else:
            return None