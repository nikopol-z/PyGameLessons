import pygame
import random


MAX_X = 1440
MAX_Y = 900
MAX_CARS = 1

class Car():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.image_filename = "C:/Users/One/Documents/PyGameLessons/static/yellow car.png"
        self.image = pygame.image.load(self.image_filename).convert_alpha()

    def move_car(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y >= 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y <= MAX_Y - 256:
            self.y += self.speed



    def draw_car(self):
        window.blit(self.image, (self.x, self.y))

def initialize_cars(MAX_CARS, cars):
    for i in range(0, MAX_CARS):
        cars.append(Car(50, 50))


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

cars = []
initialize_cars(MAX_CARS, cars)

main_running = True

while main_running:
    #win.fill(bg_color) #bg color fill
    window.blit(bg, (0,0))
    check_for_exit()
    for i in cars:
        i.move_car()
        i.draw_car()
    pygame.display.update()

pygame.quit()
