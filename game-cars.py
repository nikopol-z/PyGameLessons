import pygame
import random



class Car():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_car(self):
        #

    def draw_car(self):
        ##


def check_for_exit():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x1 >= 15:
            x1 -= speed1
            left = True
            right = False
            playerStand1[0] = pygame.transform.rotate(playerStand1[0], -1)
