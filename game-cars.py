import pygame
import random
import math
#from pygame.locals import *


MAX_X = 1440
MAX_Y = 900
CAR_SPEED = 15
MAX_CARS = 1
ROTATE_SPEED = 5
angle0 = 0

class Car():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = CAR_SPEED
        self.image_filename = "C:/Users/One/Documents/PyGameLessons/static/audi.png"
        self.image = [pygame.image.load(self.image_filename).convert(),pygame.image.load(self.image_filename).convert_alpha()]


    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        global angle0
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle + angle0)
        angle0 += angle
        angle0 %= 360
        #print (angle0)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        self.image[1] = rot_image
        #return rot_image

    def move_car(self):
        keys = pygame.key.get_pressed()
        angle1 = math.radians(angle0 + 90)
        if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            t = lambda x: -1 if x else 1
            if self.y < 0: # top border
                if math.sin(angle1) < 0:

                    self.y += self.speed * math.sin(angle1) * t(keys[pygame.K_UP])
                    #print (t(keys[pygame.K_UP]))
                    self.x += self.speed * math.cos(angle1) * t(keys[pygame.K_UP])
                    print (self.x)
                else:
                    self.x += self.speed * math.cos(angle1)
            else:   # inside the screen - going enywhere
                self.y += self.speed * math.sin(angle1) * t(keys[pygame.K_UP])
                self.x += self.speed * math.cos(angle1) * t(keys[pygame.K_UP])
            """if self.y > MAX_Y - 256: # bottom border
                if math.sin(angle1) > 0:
                    self.y -= self.speed * math.sin(angle1)
                    self.x += self.speed * math.cos(angle1)
                else:
                    self.x += self.speed * math.cos(angle1)
            else:   # inside the screen - going enywhere
                self.y -= self.speed * math.sin(angle1)
                self.x += self.speed * math.cos(angle1)

        if keys[pygame.K_DOWN]:
            if self.y <= 0 or self.y > MAX_Y - 256:
                self.y += self.speed * math.sin(angle1)
                self.x -= self.speed * math.cos(angle1)
            #print ("DOWN")
"""
        if keys[pygame.K_LEFT]:
            self.rot_center(self.image[0], ROTATE_SPEED)
        if keys[pygame.K_RIGHT]:
            self.rot_center(self.image[0], -ROTATE_SPEED)
            #self.image = pygame.transform.rotate(self.image, 1)



    def draw_car(self):
        window.blit(self.image[1], (self.x, self.y))

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
    pygame.time.delay(25)
    #pygame.display.update()
    pygame.display.flip()

pygame.quit()
