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
    def __init__(self, island):
        self.tools = []
        self.stamina = variables.TIMMY_STAMINA
        variables.CURRENT_STAMINA = self.stamina
        self.x,self.y = variables.TIMMY_CENTER
        self.color = (0,0,0)
        self.movement_speed = 0
        self.acceleration = 3
        self.info = ""
        self.island = island
        variables.CURRENT_RESSOURCES = 0
        self.timmy_sprite = pg.image.load("sprites/timmy_4x4.png")
        self.scale_factor = 4
        self.timmy_sprite = pg.transform.scale(self.timmy_sprite, (16*4*self.scale_factor,16*4*self.scale_factor))
        self.movement_sprite = (0,0,16*self.scale_factor,16*self.scale_factor)

    def upgrade_tools(self, tools):
        self.tools = tools
    
    def work(self, press, item  = None):
        if item != None:
            if press == K_SPACE and isinstance(item, Tree):
                #chop trees on island:
                if self.stamina > 0:
                    self.stamina -= 1
                    self.movement_sprite = (16*self.scale_factor, 0,16*self.scale_factor,16*self.scale_factor)
                    variables.CURRENT_STAMINA = self.stamina
                    item.work()
                    variables.CURRENT_RESSOURCES += 1
        if press == K_s:
            if isinstance(item, House):
                #Sleep:
                self.movement_speed = 0
                self.stamina = variables.TIMMY_STAMINA
                variables.CURRENT_STAMINA = self.stamina
                variables.DRAW_TEXT(self.screen)
            else:
                print("You can only sleep in the house")
                # variables.DRAW_TEXT(self.screen, "You can only sleep in the house", (200,10,10))
        elif press == K_a:
            self.movement_speed = -self.acceleration
            self.movement_sprite = (0,16*3*self.scale_factor,16*self.scale_factor,16*self.scale_factor)
        elif press == K_d:
            self.movement_speed = self.acceleration
            self.movement_sprite = (0,16*2*self.scale_factor,16*self.scale_factor,16*self.scale_factor)
        elif press == K_b and isinstance(item, House):
            if item.build_raft(variables.CURRENT_RESSOURCES):
                variables.CURRENT_RESSOURCES -= 10
        elif press == K_e and isinstance(item, Raft):
            if variables.RAFT_PIECES >= variables.RAFT_MIN_SIZE:
                draw_user_on_x = lambda screen, x: self.screen.blit(self.timmy_sprite, (x, self.y), self.movement_sprite)
                item.sail(draw_user_on_x, self.island)
            #SAIL MY BODY
    def stop(self):
        self.movement_speed = 0
        self.movement_sprite = (0,0,16*self.scale_factor,16*self.scale_factor)
    
    def get_pos(self):
        return (self.x, self.y)

    def draw(self, screen):
        self.screen = screen
        if not variables.FRAME_COUNT % 10:
            self.move()
        self.screen.blit(self.timmy_sprite, (self.x, self.y), self.movement_sprite)
        # pg.draw.circle(screen, (0,0,0), (self.x, self.y), 20)
        if self.x >= variables.ISLAND_CENTER[0]+(variables.ISLAND_WIDTH//2)+(variables.RAFT_WIDTH*variables.RAFT_PIECES) or self.x <= variables.ISLAND_CENTER[0]-(variables.ISLAND_WIDTH//2):
            self.x = variables.TIMMY_CENTER[0]
            self.stamina -= 5
            variables.CURRENT_STAMINA = self.stamina
            self.stop()
        self.x += self.movement_speed
    
    def move(self):
        next_sprite = 16*self.scale_factor
        if self.movement_speed:
            start_x = self.movement_sprite[0]+next_sprite
            if start_x >= (16*4*self.scale_factor):
                start_x = 0
            self.movement_sprite = (start_x, self.movement_sprite[1], self.movement_sprite[2], self.movement_sprite[3])

