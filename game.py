import pygame as pg
from pygame.locals import *
from island import Island
from tree import Tree
import variables

def start_screen(screen, island):
    while(True):
        screen.fill((10,10,200))
        font = pg.font.SysFont(None, 50)
        title_screen = font.render(f"Lonely Timmy", True, (0,100,100))
        center = variables.SCREEN_WIDTH//2
        y = variables.SCREEN_HEIGHT//2
        screen.blit(title_screen, (center-10*len("Lonely Timmy"), y-200))
        key = pg.event.poll()
        if key.type == KEYDOWN and key.key == K_q:
            break
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        play = font.render(f"Play", True, (200,0,0))
        
        if center+100 >= mouse[0] >= center - 100 and y+50 >= mouse[1] >= y-50:
            if click[0]:
                pg.draw.rect(screen, (0,150,0), (center-100, y-50, 200, 100))
                pg.display.flip()
                screen.blit(play, (center, y))
                pg.time.wait(100)
                break
            else:
                pg.draw.rect(screen, (0,255,0), (center-100, y-50, 200, 100))
        else:
            pg.draw.rect(screen, (0,200,0), (center-100, y-50, 200, 100))
        screen.blit(play, (center, y))
        pg.display.flip()
        

pg.init()

screen = pg.display.set_mode((variables.SCREEN_WIDTH,variables.SCREEN_HEIGHT))

island = Island(screen, [])
# island.draw()
variables.SCREEN = screen
start_screen(screen, island)
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
    variables.FRAME_COUNT += 1
    island.draw() 
    pg.display.flip()

#Exit everything
pg.quit()