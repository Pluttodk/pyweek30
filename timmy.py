from pygame.locals import *
import pygame as pg
from house import House
from tree import Tree
class Timmy:
    """
    Timmy will be our survivor, 
    based on his tools this will impact how much wood he can chop,
    and how quickly he can build the raft
    """
    def __init__(self):
        self.tools = []
        self.stamina = 10
        self.x = 200
        self.y = 420
        self.color = (0,0,0)
        self.movement_speed = 0
        self.info = ""
        self.font = pg.font.SysFont("comicsansms", 50)
        self.ressources = 0
    
    def upgrade_tools(self, tools):
        self.tools = tools
    
    def work(self, press, item  = None):
        if item != None:
            if press == K_SPACE and isinstance(item, Tree):
                #chop trees on island:
                if self.stamina > 0:
                    self.stamina -= 1
                    item.work()
                    self.ressources += 1
        if press == K_s:
            if isinstance(item, House):
                #Sleep:
                self.stamina = 10
            else:
                text = self.font.render(f"You can only sleep in house", True, (255,10,10))
                self.screen.blit(text, (0,0))
                print("you can only sleep in the house")
                #Blit does not work right now. Figure out later why
        elif press == K_a:
            self.movement_speed = -5
        elif press == K_d:
            self.movement_speed = 5
        elif press == K_b and isinstance(item, House):
            if item.build_raft(self.ressources):
                self.ressources -= 10
    def stop(self):
        self.movement_speed = 0
    
    def get_pos(self):
        return (self.x, self.y)

    def draw(self, screen):
        self.screen = screen
        text = self.font.render(f"Timmy's stamina: {self.stamina}", True, (255,255,255))
        self.screen.blit(text, (0,0))
        pg.draw.circle(screen, (0,0,0), (self.x, self.y), 20)
        self.x += self.movement_speed
