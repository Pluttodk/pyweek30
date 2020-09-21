from timmy import Timmy
from tree import Tree
import pygame as pg
import random
import numpy as np

class Island:
    background_color = (0,0,200)
    island_color = (255,137,0)

    x, y = 200,200

    def __init__(self, screen, items, level=1):
        self.screen = screen
        self.items = items
                
        self.villager = Timmy()
        # Number of trees
        self.trees = random.randint(level,level+4)
        for _ in range(self.trees):
            self.items.append(Tree())

    
    def draw(self):
        #Water
        self.screen.fill(self.background_color)
        #Island
        pg.draw.circle(self.screen, self.island_color, (500,600), 500)
        for i in self.items:
            i.draw(self.screen)
        self.villager.draw(self.screen)
    
    def work(self, press):
        x,y = self.villager.get_pos()
        has_worked = False
        for i in self.items:
            x_obj, y_obj = i.get_pos()
            diff = abs(x-x_obj)
            if diff <= 20:
                self.villager.work(press, i)
                has_worked = True
        if not has_worked:
            self.villager.work(press)
        
        
    
