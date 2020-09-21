from pygame.locals import *
import pygame as pg
class Timmy:
    """
    Timmy will be our survivor, 
    based on his tools this will impact how much wood he can chop,
    and how quickly he can build the raft
    """
    def __init__(self):
        self.tools = []
        self.stamina = 100
        self.x = 200
        self.y = 420
        self.color = (0,0,0)
        self.movement_speed = 5
    
    def upgrade_tools(self, tools):
        self.tools = tools
    
    def work(self, press, item  = None):
        if item != None:
            if press == K_SPACE:
                #chop trees on island:
                if self.stamina > 0:
                    self.stamina -= 1
                    item.chop()
        if press == K_s:
            #Sleep:
            self.stamina = 100
        elif press == K_a:
            self.x -= self.movement_speed
        elif press == K_d:
            self.x += self.movement_speed
    
    def get_pos(self):
        return (self.x, self.y)

    def draw(self, screen):
        font = pg.font.SysFont("comicsansms", 50)
        text = font.render(f"Timmy's stamina: {self.stamina}", True, (255,255,255))
        screen.blit(text, (0,0))
        pg.draw.circle(screen, (0,0,0), (self.x, self.y), 20)
