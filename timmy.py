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
        sailing = False
        if item != None:
            if press == K_SPACE and isinstance(item, Tree):
                #chop trees on island:
                if self.stamina > 0:
                    self.stamina -= 1
                    self.movement_sprite = (16*self.scale_factor, 0,16*self.scale_factor,16*self.scale_factor)
                    variables.CURRENT_STAMINA = self.stamina
                    item.work()
                    variables.CURRENT_RESSOURCES += 1
                    sound = pg.mixer.Sound("sounds/wood-hit.wav")
                    raw_array = sound.get_raw()
                    raw_array = raw_array[415000:430000]
                    cut_sound = pg.mixer.Sound(buffer=raw_array)
                    cut_sound.set_volume(1)
                    cut_sound.play()
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
        elif press == K_a or press == K_LEFT:
            self.movement_speed = -self.acceleration
            self.movement_sprite = (0,16*3*self.scale_factor,16*self.scale_factor,16*self.scale_factor)
        elif press == K_d or press == K_RIGHT:
            self.movement_speed = self.acceleration
            self.movement_sprite = (0,16*2*self.scale_factor,16*self.scale_factor,16*self.scale_factor)
        elif press == K_b and isinstance(item, House):
            if item.build_raft(variables.CURRENT_RESSOURCES):
                variables.CURRENT_RESSOURCES -= variables.RAFT_COST
        elif press == K_e and isinstance(item, Raft):
            if variables.RAFT_PIECES >= variables.RAFT_MIN_SIZE:
                draw_user_on_x = lambda screen, x: self.screen.blit(self.timmy_sprite, (x-(self.scale_factor*16)//2, self.y), self.movement_sprite)
                item.sail(draw_user_on_x, self.island)
                self.x = variables.ISLAND_CENTER[0]
                variables.RAFT_PIECES = 0
                sailing = True
        return sailing
            #SAIL MY BODY
    def stop(self):
        self.movement_speed = 0
        self.movement_sprite = (0,0,16*self.scale_factor,16*self.scale_factor)
    
    def get_pos(self):
        return (self.x+(16*self.scale_factor)//2, self.y)

    def die(self):
        self.stamina = 0
        variables.CURRENT_STAMINA = 0

    def draw(self, screen):
        self.screen = screen
        if not variables.FRAME_COUNT % 10:
            self.move()
        self.screen.blit(self.timmy_sprite, (self.x, self.y), self.movement_sprite)
        # pg.draw.circle(screen, (0,0,0), (self.x, self.y), 20)
        if (self.x+16*self.scale_factor) >= variables.ISLAND_CENTER[0]+(variables.ISLAND_WIDTH//2)+(variables.RAFT_WIDTH*variables.RAFT_PIECES*2) or self.x <= variables.ISLAND_CENTER[0]-(variables.ISLAND_WIDTH//2):
            self.die()
            return "Watch out for the water. Timmy can only swim if he has Stamina"
        self.x += self.movement_speed
        return ""
    
    def move(self):
        next_sprite = 16*self.scale_factor
        if self.movement_speed:
            start_x = self.movement_sprite[0]+next_sprite
            if start_x >= (16*4*self.scale_factor):
                start_x = 0
            self.movement_sprite = (start_x, self.movement_sprite[1], self.movement_sprite[2], self.movement_sprite[3])

