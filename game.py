import pygame as pg
from pygame.locals import *
from island import Island
from tree import Tree
import variables

pg.init()

screen = pg.display.set_mode((variables.SCREEN_WIDTH,500))

island = Island(screen, [])
island.draw()
variables.SCREEN = screen
#Game loop
while(True):
    key = pg.event.poll()
    start_level = variables.LEVEL
    if key.type == KEYDOWN:
        if key.key == K_q:
            break
        elif key.key == K_r:
            island = Island(screen, [])
        else:
            island.work(key.key)
    elif key.type == KEYUP:
        if key.key == K_a or key.key == K_d:
            island.villager.stop()
    if start_level != variables.LEVEL:
        island = Island(screen, [], level=variables.LEVEL)
    island.draw() 
    pg.display.flip()

#Exit everything
pg.quit()