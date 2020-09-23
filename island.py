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
    island_color = (255,137,0)

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
        variables.DAY = 0

        if level == 1:
            # For the first level, simply add the raft criteria to be 1
            self.raft_criteria = 4

    def draw(self, is_sailing=False):
        #Water
        self.screen.fill(self.background_color)
        #Island
        pg.draw.circle(self.screen, self.island_color, (500,500), variables.ISLAND_WIDTH//2)
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
            self.screen.fill((color))

            
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
            pg.draw.circle(self.screen, sun_color, (sun_x, sun_y), sun_width)
            

            #Island
            pg.draw.circle(self.screen, self.island_color, (500,500), variables.ISLAND_WIDTH//2)
            for j in self.items:
                j.draw(self.screen)
            self.villager.draw(self.screen)

            pg.time.delay(10)
            pg.display.flip()
        variables.DAY += 1
    
    
