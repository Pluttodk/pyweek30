import pygame as pg
from pygame.locals import *
from island import Island
from tree import Tree
import variables

def play_game(screen):
    island = Island(screen, [])
    #Game loop
    while(True):
        key = pg.event.poll()
        start_level = variables.LEVEL
        if key.type == KEYDOWN:
            if key.key == K_ESCAPE:
                should_close, updated_data = pause_screen(screen)
                if updated_data != None:
                    island = updated_data
                if should_close:
                    return
            elif key.key == K_r:
                island = Island(screen, [])
            else:
                island.work(key.key)
        elif key.type == pg.QUIT:
            return
        elif key.type == KEYUP:
            if key.key == K_a or key.key == K_d:
                island.villager.stop()
        if start_level != variables.LEVEL:
            island = Island(screen, [], level=variables.LEVEL)
        variables.FRAME_COUNT += 1
        island.draw() 
        pg.display.flip()

def start_screen(screen):
    while(True):
        font = pg.font.SysFont(None, 40)
        title_screen = pg.image.load("sprites/title_screen.png")
        center = variables.SCREEN_WIDTH//2
        y = (variables.SCREEN_HEIGHT//2)+100
        screen.blit(title_screen, (0,0))
        key = pg.event.poll()
        if key.type == KEYDOWN and (key.key == K_ESCAPE):
            return
        elif key.type == pg.QUIT:
            return
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        play = font.render(f"Play", True, (255, 255, 255))
        settings = font.render(f"How to play", True, (255, 255, 255))
        play_rect = play.get_rect()
        settings_rect = settings.get_rect()
        if center+100 >= mouse[0] >= center - 100 and y+50 >= mouse[1] >= y-50:
            if click[0]:
                pg.draw.rect(screen, (0,0,0), (center-100, y-50, 200, 100))
                screen.blit(play, (center-play_rect.width//2, y-play_rect.height//2))
                y += 100
                pg.draw.rect(screen, (10,10,10), (center-100, y-30, 200,60))
                screen.blit(settings, (center-settings_rect.width//2, y-settings_rect.height//2))
                pg.display.flip()
                pg.time.wait(100)
                play_game(screen)
                return
            else:
                pg.draw.rect(screen, (20,20,20), (center-100, y-50, 200, 100))
        else:
            pg.draw.rect(screen, (10,10,10), (center-100, y-50, 200, 100))
        screen.blit(play, (center-play_rect.width//2, y-play_rect.height//2))
        y += 100
        if center+100 >= mouse[0] >= center - 100 and y+30 >= mouse[1] >= y-30:
            if click[0]:
                pg.draw.rect(screen, (0,0,0), (center-100, y-30, 200,60))
                screen.blit(settings, (center-settings_rect.width//2, y-settings_rect.height//2))
                y -= 100
                pg.draw.rect(screen, (10,10,10), (center-100, y-50, 200, 100))
                screen.blit(play, (center-play_rect.width//2, y-play_rect.height//2))
                pg.display.flip()
                pg.time.wait(100)
                settings_screen(screen)
                return
            else:
                pg.draw.rect(screen, (20,20,20), (center-100, y-30, 200,60))
        else:
            pg.draw.rect(screen, (10,10,10), (center-100, y-30, 200,60))
        screen.blit(settings, (center-settings_rect.width//2, y-settings_rect.height//2))
        pg.display.flip()

def pause_screen(screen):
    title_screen = pg.image.load("sprites/pause_screen.png")
    font = pg.font.SysFont(None, 40)
    resume = font.render("Resume", True, (255,255,255))
    how = font.render("How to play", True, (255,255,255))
    restart = font.render("Restart", True, (255,255,255))
    end = font.render("Exit", True, (255,255,255))
    text = [(resume, lambda: (False, None)), (how, lambda s=screen: (settings_screen(screen, True), None)), (restart, lambda s=screen: (False, Island(screen, []))), (end, lambda: (True, None))]
    while(True):
        key = pg.event.poll()
        center = variables.SCREEN_WIDTH//2
        padding = (variables.SCREEN_HEIGHT//15)
        y = variables.SCREEN_HEIGHT//4 + padding
        screen.blit(title_screen, (0,0))
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        for t,action in text:
            color = (10,10,10) if not (center+100 >= mouse[0] >= center-100 and y+30 >= mouse[1] >= y-30)  else ((20,20,20) if not click[0] else (0,0,0))
            pg.draw.rect(screen, color, (center-100, y-30, 200, 60))
            screen.blit(t, (center-t.get_rect().width//2, y-t.get_rect().height//2))
            if color == (0,0,0):
                pg.time.wait(100)
                return action()
            y += 60 + padding
        if key.type == KEYDOWN and (key.key == K_ESCAPE):
            return False
        elif key.type == pg.QUIT:
            return True
        pg.display.flip()

def settings_screen(screen, is_paused=False):
    info_1 = pg.image.load("sprites/info_1.png")
    info_2 = pg.image.load("sprites/info_2.png")
    font = pg.font.SysFont(None, 40)
    center = variables.SCREEN_WIDTH//2
    y = (variables.SCREEN_HEIGHT//2)+100
    screen_id = 1
    if is_paused:
        play = font.render(f"Continue", True, (255, 255, 255))
    else:
        play = font.render(f"Play", True, (255, 255, 255))
    nxt = font.render(f"Next", True, (255, 255, 255))
    ext = font.render(f"Exit", True, (255, 255, 255))
    nxt_screen = False
    ext_screen = False
    while(True):
        key = pg.event.poll()
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        color1 = (10,10,10)
        color2 = (10,10,10)
        if center+100 >= mouse[0] >= center - 100 and y+30 >= mouse[1] >= y-30:
            color1 = (0,0,0) if click[0] else (20,20,20)
            if click[0]:
                nxt_screen = True
        elif center+100 >= mouse[0] >= center - 100 and y+120 >= mouse[1] >= y+60:
            color2 = (0,0,0) if click[0] else (20,20,20)
            if click[0]:
                ext_screen = True
        if screen_id == 1:
            screen.blit(info_1, (0,0))
            pg.draw.rect(screen, color1, (center-100, y-30, 200, 60))
            screen.blit(nxt, (center-nxt.get_rect().width//2, y-nxt.get_rect().height//2))
        else:
            screen.blit(info_2, (0,0))
            pg.draw.rect(screen, color1, (center-100, y-30, 200, 60))
            screen.blit(play, (center-play.get_rect().width//2, y-play.get_rect().height//2))

        pg.draw.rect(screen, color2, (center-100, y+60, 200, 60))
        screen.blit(ext, (center-ext.get_rect().width//2, y+90-ext.get_rect().height//2))
        if key.type == KEYDOWN and (key.key == K_ESCAPE):
            return
        elif key.type == pg.QUIT:
            return
        if nxt_screen:
            pg.time.wait(100)
            nxt_screen = False
            if screen_id == 2:
                if is_paused:
                    return False
                play_game(screen)
                return
            screen_id = 2
        elif ext_screen:
            pg.time.wait(50)
            ext_screen = False
            if is_paused:
                return False
            start_screen(screen)
            return
        pg.display.flip()


pg.init()

screen = pg.display.set_mode((variables.SCREEN_WIDTH,variables.SCREEN_HEIGHT))

# island.draw()
variables.SCREEN = screen
start_screen(screen)



#Exit everything
pg.quit()