import pygame as pg
ISLAND_WIDTH = 800
ISLAND_CENTER = (500,500)
ISLAND_DECAY = 60

TIMMY_CENTER = (400,370)
TIMMY_STAMINA = 30

HOUSE_CENTER = (500,300)

RAFT_LOCATION = (ISLAND_CENTER[0] + ISLAND_WIDTH//2,400)
RAFT_COST = 10
RAFT_WIDTH = 12
RAFT_PIECES = 0
RAFT_HEIGHT = 50
RAFT_SPACING = 1
RAFT_MIN_SIZE = 4

RANGE = 5
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500


CURRENT_STAMINA = TIMMY_STAMINA
CURRENT_RESSOURCES = 0
DAY = 1
LEVEL = 1

LEVEL_RAFT = [4,8,12,16] # Leaving for a total number of ress = 400
LEVEL_TREES = [8,6,4,2]
LEVEL_TREES_RESSOURCES = [200,120,80,50] # The number of trees ressources to be available from the begining (This will mean that you will have to farm all at first level. Even though that grows during night)
LEVEL_ISLAND_SIZE = [800,600,400,300]

FRAME_COUNT = 0

STAMINA_BAR = pg.image.load("sprites/stamina_outline.png")
STAMINA_FILL = pg.image.load("sprites/stamina_fill.png")
RESSOURCES = pg.image.load("sprites/Lumber.png")
BORDER = pg.image.load("sprites/border.png")
TEXT_COLOR = (10,10,10)
_circle_cache = {}

def DRAW_TEXT(screen, info="", color=TEXT_COLOR):
    font = pg.font.SysFont(None, 30)
    font2 = pg.font.SysFont(None, 25)
    if not len(info):
        stamina = render(f"Stamina", font, TEXT_COLOR)
        # stamina = font.render(f"Stamina", True, TEXT_COLOR)
        ressources = render(f"{CURRENT_RESSOURCES}", font, TEXT_COLOR)
        day = render(f"Day: {DAY}", font, TEXT_COLOR)
        boat = render(f"Boat: {RAFT_PIECES}/{RAFT_MIN_SIZE} ", font, TEXT_COLOR)
        level = render(f"Island: {LEVEL}", font2, TEXT_COLOR)

        screen.blit(BORDER, (0,0))

        screen.blit(STAMINA_BAR, (10,10))
        procentage = (CURRENT_STAMINA/TIMMY_STAMINA)
        screen.blit(STAMINA_FILL, (10,10), (0,0, procentage*STAMINA_FILL.get_width(), STAMINA_FILL.get_height()))
        screen.blit(stamina, (70,20))
        # screen.blit(stamina, (0,0))
        screen.blit(RESSOURCES, (217, 10))
        if CURRENT_RESSOURCES < 10:
            screen.blit(ressources, (230,20))
        else:
            screen.blit(ressources, (227,20))
        screen.blit(day, (273,20))
        screen.blit(boat, (353,20))
        screen.blit(level, (SCREEN_WIDTH-80,20))

    else:
        text = font.render(info, True, color, (0,0,0))
        screen.blit(text, (600,0))

# Taken directly from https://stackoverflow.com/questions/54363047/how-to-draw-outline-on-the-fontpygame
def _circlepoints(r):
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points

def render(text, font, gfcolor=pg.Color('dodgerblue'), ocolor=(255, 255, 255), opx=2):
    textsurface = font.render(text, True, gfcolor).convert_alpha()
    w = textsurface.get_width() + 2 * opx
    h = font.get_height()

    osurf = pg.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))

    surf = osurf.copy()

    osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))

    for dx, dy in _circlepoints(opx):
        surf.blit(osurf, (dx + opx, dy + opx))

    surf.blit(textsurface, (opx, opx))
    return surf