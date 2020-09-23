import pygame as pg
ISLAND_WIDTH = 800
ISLAND_CENTER = (500,500)

TIMMY_CENTER = (400,370)
TIMMY_STAMINA = 20

HOUSE_CENTER = (200,420)

RAFT_LOCATION = (ISLAND_CENTER[0] + ISLAND_WIDTH//2,400)
RAFT_COST = 10
RAFT_WIDTH = 12
RAFT_PIECES = 0
RAFT_HEIGHT = 50
RAFT_SPACING = 1
RAFT_MIN_SIZE = 4

RANGE = 20
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500


CURRENT_STAMINA = TIMMY_STAMINA
CURRENT_RESSOURCES = 0
DAY = 0
LEVEL = 1

FRAME_COUNT = 0

def DRAW_TEXT(screen, info="", color=(255,255,255)):
    font = pg.font.SysFont(None, 50)
    if not len(info):
        stamina = font.render(f"Timmy's stamina: {CURRENT_STAMINA}", True, (255,255,255), (0,0,0))
        ressources = font.render(f"Ressources: {CURRENT_RESSOURCES}", True, (255,255,255), (0,0,0))
        day = font.render(f"Day: {DAY}", True, (255,255,255), (0,0,0))
        boat = font.render(f"Boat: {RAFT_PIECES}/{RAFT_MIN_SIZE} ", True, (255,255,255), (0,0,0))
        level = font.render(f"Level: {LEVEL}", True, (255,255,255), (0,0,0))
        screen.blit(stamina, (0,0))
        screen.blit(ressources, (0,50))
        screen.blit(day, (0,100))
        screen.blit(boat, (0,150))
        screen.blit(level, (0,200))

    else:
        text = font.render(info, True, color, (0,0,0))
        screen.blit(text, (600,0))