import pygame, time
import numpy as np

vec = pygame.math.Vector2

class LineOfDroplets(pygame.sprite.Sprite):
    def __init__(self, length, list_of_01, v0 = vec(0, 0), a = vec(0,9.81)):
        pygame.sprite.Sprite.__init__(self)
        self.size = (length, int(1.77*length/len(list_of_01)))
        self.position = vec(self.size[0] / 2, self.size[1] / 2)
        self.image = pygame.Surface(self.size)
        self.image.fill((255,255,255))
        self.droplet_img = pygame.transform.scale(pygame.image.load("./src/droplet.png"),(int(self.image.get_width()/len(list_of_01)),self.image.get_height()))
        self.create_line(list_of_01)
        self.rect = self.image.get_rect(center=self.position)
        self.a = a*10
        self.v0 = v0*10
        self.last_update = time.time()

    def create_line(self, list_of_01):
        n = len(list_of_01)
        width = self.image.get_width()/n
        height = self.image.get_height()
        for i in range(n):
            if list_of_01[i] != 0:
                self.image.blit(self.droplet_img, (i*width,0))
                # pygame.draw.rect(self.image, pygame.Color(0,0,0), pygame.Rect(i*width,0, width, height))
            else:
                pygame.draw.rect(self.image, pygame.Color(255,255,255), pygame.Rect(i*width,0, width, height))

    def update(self):
        now = time.time()
        duration = now - self.last_update
        distance = 0.5*self.a*(duration**2)+self.v0*(duration)
        self.v0 += duration*self.a
        self.position += distance 
        self.rect.center = self.position
        self.last_update = now
