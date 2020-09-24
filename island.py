from timmy import Timmy
from tree import Tree
import pygame as pg
from pygame.locals import K_s
import random
import numpy as np
import variables
from house import House
import time

class Island:
    background_color = (10,10,200)
    background_image = "sprites/background.png"
    island_color = (255,137,0)
    island_image = "sprites/islands.png"

    x, y = 200,200

    def __init__(self, screen, items, level=1):
        self.screen = screen
        self.items = items
                
        self.villager = Timmy(self)
        # Number of trees
        self.trees = random.randint(level,level+4)
        variables.RAFT_MIN_SIZE = level*4
        for _ in range(self.trees):
            self.items.append(Tree())
        self.items.append(House())
        variables.DAY = 1
        self.bkg = pg.image.load(self.background_image)
        self.isl = pg.image.load(self.island_image)
        if level == 1:
            # For the first level, simply add the raft criteria to be 1
            self.raft_criteria = 4

    def draw(self, is_sailing=False):
        #Water
        self.screen.blit(self.bkg, (0,0))
        filt = pg.Surface((self.bkg.get_width(), self.bkg.get_height()), flags=pg.SRCALPHA)
        filt.fill((255, 255, 255, 1))
        #Island
        # pg.draw.circle(self.screen, self.island_color, (500,500), variables.ISLAND_WIDTH//2)
        self.isl = pg.transform.scale(self.isl, (variables.ISLAND_WIDTH, variables.ISLAND_WIDTH))
        self.screen.blit(self.isl, (500-variables.ISLAND_WIDTH//2,500 -variables.ISLAND_WIDTH//2))

        for i in self.items:
            if isinstance(i, House):
                i.draw(self.screen, is_sailing)
            else:
                i.draw(self.screen)
        if not is_sailing:
            self.villager.draw(self.screen)
        variables.DRAW_TEXT(self.screen)
    
    def work(self, press):
        x,y = self.villager.get_pos()
        has_worked = False
        for i in self.items:
            if i.is_dead():
                self.items.remove(i)
            else:
                obj = i.calc_nearest_object(x)
                if obj != None:
                    self.villager.work(press, obj)
                    if isinstance(obj, House) and press == K_s:
                        self.sleep()
                    has_worked = True
        if not has_worked:
            self.villager.work(press)
    
    def sleep(self):
        cycle = np.hstack((np.linspace(1,100,100),np.linspace(100,1,100)))
        for i,v in enumerate(cycle):
            color = np.asarray(self.background_color)
            color += int(v)
            color = map(lambda x: 0 if x < 0 else (255 if x > 255 else x),color)
            color = tuple(color)
            #Water
            filt = pg.Surface((self.bkg.get_width(), self.bkg.get_height()), flags=pg.SRCALPHA)
            filt.fill((255, 255, 255, v))
            self.screen.blit(self.bkg, (0,0))
            self.screen.blit(filt, (0, 0))
            # self.screen.fill((color))

            
            sun_x = int(variables.SCREEN_WIDTH * (i/190))
            sun_color = (255,255,0)
            sun_width = 40
            c = 1000/2
            b = 600
            a = b/(c**2)
            # Formula found here: https://www.desmos.com/calculator/awtnrxh6rk
            # Used to create paraboula based on width and height
            y = int(-(a*(((i/200)*1000)-c)**2)+b)
            sun_y = abs((b+sun_width)-y)
            
            self.isl = pg.transform.scale(self.isl, (variables.ISLAND_WIDTH, variables.ISLAND_WIDTH))
            self.screen.blit(self.isl, (500-variables.ISLAND_WIDTH//2,500 -variables.ISLAND_WIDTH//2))

            #Island
            # pg.draw.circle(self.screen, self.island_color, (500,500), variables.ISLAND_WIDTH//2)
            for j in self.items:
                j.draw(self.screen)
            self.villager.draw(self.screen)
            pg.draw.circle(self.screen, sun_color, (sun_x, sun_y), sun_width)
            pg.time.delay(10)
            pg.display.flip()
        variables.ISLAND_WIDTH -= 200
        variables.DAY += 1
    
    
