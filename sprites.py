# sprites classes for game

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *

vec = pg.math.Vector2

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(BLACK)
        #very powerful allows screen to see where the sprite is
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = (0, 0)
        self.acc = (0, 0)
        
    def update(self):
        self.acc = vec(0, 0)
       
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        self.vel += self.acc
        self.pos += self.vel + PLAYER_ACC * self.acc

        self.rect.center = self.pos
        # if keys[pg.K_UP] and self.falling == False:
        #     self.jump()
        # self.vy = 0
        # if keys[pg.K_UP]:
        #     self.vy = -5
        # if keys[pg.K_DOWN]:
        #     self.vy = 5
        
        # self.rect.x += self.vx
        # self.rect.y += self.vy
    
    # def gravity(self):
    #     #have to figure out how to make this kick in
    #     if self.rect.y < HEIGHT-40:
    #         self.falling = True
    #         self.vy += 10
    #     elif self.rect.y >= HEIGHT:
    #         self.falling = False
    #         self.vy = 0
    #         self.rect.y = HEIGHT-40
    #         print("falling " + str(self.falling))
    # def jump(self):
    #     #has to look like someone jumping
    #    self.vy = -75
    #    print("jumping")
        
# class Enemy(Sprite):
#     def __init__(self):
#         Sprite.__init__(self)
#         self.image = pg.Surface((30,40))
#         self.image.fill(WHITE)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH / 2, HEIGHT / 2)
#         self.vx = 0
#         self.vy = 0
