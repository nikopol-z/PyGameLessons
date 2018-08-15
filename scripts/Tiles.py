import pygame

pygame.init()


class Tiles:

    size = 32

    def load_texture(file, size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (size, size))
        #'C:\\Users\\One\\Documents\\PyGameLessons\\scripts\\grass1.jpg'

        surface = pygame.Surface((size, size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0,0))
        return surface

    Grass1 = load_texture("GRAPHICS\\grass1.jpg", size)

    Grass2 = load_texture("graphics\\grass2.jpg", size)

    Grass = load_texture("graphics\\grass.png", size)

    Stone = load_texture("graphics\\stone.png", size)

    Water = load_texture("graphics\\water.png", size)

    Texture_Tags = {"1" : Grass, "2" : Stone, "3" : Water}
