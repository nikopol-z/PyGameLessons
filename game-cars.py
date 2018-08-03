import pygame
import random


MAX_X = 1440
MAX_Y = 900

class Car():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_car(self):
        i = 2


    def draw_car(self):
        j = 3


def check_for_exit():
    global main_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #sys.exit()
            main_running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            #sys.exit()
            main_running = False



# ---------------------------- MAIN ---------------------------
pygame.init()
window = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (0, 0, 0)
bg = pygame.image.load('C:/Users/One/Documents/PyGameLessons/parking.png')
bg = pygame.transform.scale(bg, (MAX_X, MAX_Y))
main_running = True

while main_running:
    #win.fill(bg_color) #bg color fill
    window.blit(bg, (0,0))
    check_for_exit()
    pygame.display.update()

pygame.quit()
