import pygame as pg
ISLAND_WIDTH = 800
ISLAND_CENTER = (500,500)

TIMMY_CENTER = (400,420)
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


CURRENT_STAMINA = TIMMY_STAMINA
CURRENT_RESSOURCES = 0
DAY = 0
LEVEL = 1

def DRAW_TEXT(screen, info="", color=(255,255,255)):
    font = pg.font.SysFont("comicsansms", 50)
    if not len(info):
        text = font.render(f"Timmy's stamina: {CURRENT_STAMINA}, Ressources: {CURRENT_RESSOURCES}, Day: {DAY}, Boat: {RAFT_PIECES}/{RAFT_MIN_SIZE}, Level: {LEVEL}", True, (255,255,255), (0,0,0))
        screen.blit(text, (0,0))
    else:
        text = font.render(info, True, color, (0,0,0))
        screen.blit(text, (600,0))