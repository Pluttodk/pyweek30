from timmy import Timmy
from tree import Tree
import pygame as pg
from pygame.locals import K_s
import random
import numpy as np
import variables
from house import House
import time
import numpy as np

class Island:
    background_color = (10,10,200)
    background_image = "sprites/background.png"
    island_color = (255,137,0)
    island_image = "sprites/islands.png"

    x, y = 200,200
    
    def __init__(self, screen, items, level=1):
        self.screen = screen
        self.items = items
        variables.DAY = 1
        variables.LEVEL = 1
        variables.RAFT_PIECES = 0
        self.villager = Timmy(self)
        # Number of trees
        # This will ensure that the sum will always be the same for each run
        self.new_level()

    def new_level(self):
        self.items = []
        if variables.LEVEL == 5:
            return
        variables.ISLAND_WIDTH = variables.LEVEL_ISLAND_SIZE[variables.LEVEL-1]
        n = variables.LEVEL_TREES[variables.LEVEL-1]
        sizes = np.random.multinomial(variables.LEVEL_TREES_RESSOURCES[variables.LEVEL-1], np.ones(n)/n, size=1)[0]
        part1_trees = np.linspace(variables.ISLAND_CENTER[0]-variables.ISLAND_WIDTH//3, variables.ISLAND_CENTER[0]-100, n//2)
        part2_trees = np.linspace(variables.ISLAND_CENTER[0]+100, variables.ISLAND_CENTER[0]+variables.ISLAND_WIDTH//3, n//2)
        trees_pos = np.hstack((part1_trees,part2_trees))
        for s,x in zip(sizes, trees_pos):
            self.items.append(Tree(s, x))
        self.items.append(House())

        self.bkg = pg.image.load(self.background_image)
        self.isl = pg.image.load(self.island_image)
        variables.RAFT_MIN_SIZE = variables.LEVEL_RAFT[variables.LEVEL-1]


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
            mess = self.villager.draw(self.screen)
            if len(mess):
                return mess
        variables.DRAW_TEXT(self.screen)
        return ""
    
    def work(self, press):
        x,y = self.villager.get_pos()
        has_worked = False
        contains_tree = False
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
                if isinstance(i, Tree):
                    contains_tree = True
        if not has_worked:
            self.villager.work(press)
        if not contains_tree and (variables.CURRENT_RESSOURCES < variables.RAFT_COST and variables.RAFT_PIECES < variables.RAFT_MIN_SIZE):
            return "No more trees left. Plan your ressources more cautios"
        return ""
    
    def sleep(self):
        cycle = np.hstack((np.linspace(51,150,100),np.linspace(150,51,100)))
        for i,v in enumerate(cycle):
            color = np.asarray(self.background_color)
            color += int(v)
            color = map(lambda x: 0 if x < 0 else (255 if x > 255 else x),color)
            color = tuple(color)
            #Water
            filt = pg.Surface((self.bkg.get_width(), self.bkg.get_height()), flags=pg.SRCALPHA)
            filt.fill((0,0,0, v))
            self.screen.blit(self.bkg, (0,0))
            # self.screen.fill((color))

            
            sun_x = int(variables.SCREEN_WIDTH * (i/190))
            sun_color = (150,150,150)
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
            self.screen.blit(filt, (0, 0))

            pg.time.delay(3)
            pg.display.flip()
        variables.ISLAND_WIDTH -= variables.ISLAND_DECAY
        for i in self.items:
            x,_ = i.get_pos()
            if variables.ISLAND_CENTER[0]+variables.ISLAND_WIDTH//3 >= x >= variables.ISLAND_CENTER[0]-variables.ISLAND_WIDTH//3:
                i.life += random.randint(1,4)
            else:
                i.life = 0
                self.items.remove(i)
        variables.DAY += 1
    
    
