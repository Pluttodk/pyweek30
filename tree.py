import random
import pygame as pg
import variables 

class Tree:
    start_y = 400
    color = (255, 213, 0)
    def __init__(self):
        self.life = random.randint(30,100)
        low_x = variables.ISLAND_CENTER[0]-int(variables.ISLAND_WIDTH//2*0.8)
        high_x = variables.ISLAND_CENTER[0]+int(variables.ISLAND_WIDTH//2*0.8)
        self.x = random.randint(low_x, high_x)
    
    def work(self):
        if self.life > 0:
            self.life -= 1
    
    def draw(self, screen):
        x = self.x
        y = self.start_y
        for i in range(self.life):
            y -= 3
            width = 10
            height = 3
            pg.draw.rect(screen, self.color, (x,y,width, height))
        y -= 3
        pg.draw.circle(screen, (0,200,0), (x+6,y), 10)
    
    def get_pos(self):
        return (self.x, self.start_y)
    
    def is_dead(self):
        return self.life <= 0
    
    def calc_nearest_object(self, x):
        diff = abs(x-self.x)
        if diff <= variables.RANGE:
            return self
        else:
            return None