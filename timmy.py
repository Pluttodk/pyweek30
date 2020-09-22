from pygame.locals import *
import pygame as pg
from house import House
from raft import Raft
from tree import Tree
import variables
class Timmy:
    """
    Timmy will be our survivor, 
    based on his tools this will impact how much wood he can chop,
    and how quickly he can build the raft
    """
    def __init__(self):
        self.tools = []
        self.stamina = variables.TIMMY_STAMINA
        variables.CURRENT_STAMINA = self.stamina
        self.x,self.y = variables.TIMMY_CENTER
        self.color = (0,0,0)
        self.movement_speed = 0
        self.acceleration = 3
        self.info = ""
        variables.CURRENT_RESSOURCES = 0
    
    def upgrade_tools(self, tools):
        self.tools = tools
    
    def work(self, press, item  = None):
        if item != None:
            if press == K_SPACE and isinstance(item, Tree):
                #chop trees on island:
                if self.stamina > 0:
                    self.stamina -= 1
                    variables.CURRENT_STAMINA = self.stamina
                    item.work()
                    variables.CURRENT_RESSOURCES += 1
        if press == K_s:
            if isinstance(item, House):
                #Sleep:
                self.stamina = variables.TIMMY_STAMINA
            else:
                print("You can only sleep in the house")
                # variables.DRAW_TEXT(self.screen, "You can only sleep in the house", (200,10,10))
        elif press == K_a:
            self.movement_speed = -self.acceleration
        elif press == K_d:
            self.movement_speed = self.acceleration
        elif press == K_b and isinstance(item, House):
            if item.build_raft(variables.CURRENT_RESSOURCES):
                variables.CURRENT_RESSOURCES -= 10
        elif press == K_e:
            print(item)
            #SAIL MY BODY
            print("SAILING!!!")
    def stop(self):
        self.movement_speed = 0
    
    def get_pos(self):
        return (self.x, self.y)

    def draw(self, screen):
        self.screen = screen
        pg.draw.circle(screen, (0,0,0), (self.x, self.y), 20)
        if self.x >= variables.ISLAND_CENTER[0]+(variables.ISLAND_WIDTH//2)+(variables.RAFT_WIDTH*variables.RAFT_PIECES) or self.x <= variables.ISLAND_CENTER[0]-(variables.ISLAND_WIDTH//2):
            self.x = variables.TIMMY_CENTER[0]
            self.stamina -= 5
            variables.CURRENT_STAMINA = self.stamina
            self.stop()
        self.x += self.movement_speed
