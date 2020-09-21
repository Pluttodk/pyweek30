import random
import pygame as pg

class Tree:
    start_y = 400
    color = (255, 213, 0)
    def __init__(self):
        self.life = random.randint(30,100)
        self.start_x = random.randint(100, 900)
    
    def work(self):
        if self.life > 0:
            self.life -= 1
    
    def draw(self, screen):
        x = self.start_x
        y = self.start_y
        for i in range(self.life):
            y -= 3
            width = 10
            height = 3
            pg.draw.rect(screen, self.color, (x,y,width, height))
        y -= 3
        pg.draw.circle(screen, (0,200,0), (x+6,y), 10)
    
    def get_pos(self):
        return (self.start_x, self.start_y)