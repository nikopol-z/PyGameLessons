import pygame, sys, time
from scripts.UltraColor import *

pygame.init()

crnSec = 0
crnFrame = 0
FPS = 0
tile_size = 32

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

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
    global crnSec, crnFrame, FPS

    if crnSec == time.strftime("%S"):
        crnFrame += 1
    else:
        FPS = crnFrame
        crnFrame = 0
        crnSec = time.strftime("%S")


create_main_window()

isRunning = True

# -------------------- MAIN LOOP ----------------------------------

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # ---------------- LOGIC --------------------------------------
    count_FPS()


    # ---------------- RENDER GRAPHICS ----------------------------
    wndw.fill((Color.Black))

    # ---------------- RENDER SIMPLE TERRAIN GRID -----------------
    for x in range(0, 640, tile_size):
        for y in range(0, 480, tile_size):
            pygame.draw.rect(wndw, Color.White, (x, y, tile_size + 1, tile_size + 1), 1)

    show_FPS()

    pygame.display.update()


pygame.quit()
sys.exit()
