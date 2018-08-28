import pygame, sys, time
from scripts.UltraColor import *
from scripts.Tiles import *
from scripts.Globals import *
from scripts.map_engine import *

pygame.init()

crnSec = 0
crnFrame = 0
FPS = 0



#clock = pygame.time.Clock()

#map_data = [(5, 6, "2"), (7, 2, "3")]

terrain = Map_Engine.load_map("maps\\world.map")


fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

sky = pygame.image.load("graphics\\sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky

def show_FPS():
    fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
    wndw.blit(fps_overlay, (0, 0))

def create_main_window():
    global wndw, win_height, win_width, win_title
    win_width, win_height = 800, 600
    win_title = "Youtube RPG"
    pygame.display.set_caption(win_title)
    wndw = pygame.display.set_mode((win_width, win_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

def count_FPS():
    global crnSec, crnFrame, FPS, deltatime

    if crnSec == time.strftime("%S"):
        crnFrame += 1
    else:
        FPS = crnFrame
        crnFrame = 0
        crnSec = time.strftime("%S")
        if FPS > 0:
            deltatime = 1 / FPS


create_main_window()

isRunning = True

# -------------------- MAIN LOOP ----------------------------------

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.cam_move = 1
            elif event.key == pygame.K_s:
                Globals.cam_move = 2
            elif event.key == pygame.K_a:
                Globals.cam_move = 3
            elif event.key == pygame.K_d:
                Globals.cam_move = 4
        elif event.type == pygame.KEYUP:
            Globals.cam_move = 0

    # ---------------- LOGIC --------------------------------------
    if Globals.cam_move == 1:
        Globals.cam_y += 100 * deltatime
    if Globals.cam_move == 2:
        Globals.cam_y -= 100 * deltatime
    if Globals.cam_move == 3:
        Globals.cam_x += 100 * deltatime
    if Globals.cam_move == 4:
        Globals.cam_x -= 100 * deltatime


    # ---------------- RENDER GRAPHICS ----------------------------
    #wndw.fill((Color.Black))
    wndw.blit(Sky, (0, 0))

    wndw.blit(terrain, (Globals.cam_x, Globals.cam_y))

    # ---------------- RENDER SIMPLE TERRAIN GRID -----------------




    show_FPS()

    pygame.display.update()

    count_FPS()

    #clock.tick(100)

pygame.quit()
sys.exit()
