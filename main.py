#thsi file was created by Zane Hake
#sources: goo.gl/2KMivS

import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("jumpy")
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        #add all sprits to the group of pg
        self.all_sprites = pg.sprite.Group()
        # adds a player to the group
        self.player = Player()
        self.all_sprites.add(self.player)
        # self.enemy = Enemy()
        # self.all_sprites.add(self.enemy)
        #call the method to run
        self.run()
    def run(self):
        #very imporrtant allows for sprite to move thru screen
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        self.all_sprites.update()
    def events(self):
        #listening for evernts
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    #makes screen red
    def draw(self):
        self.screen.fill(REDDISH)
        #very important uses all sprites
        self.all_sprites.draw(self.screen)
        #decreases lag by making loading next display in memory
        pg.display.flip()
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()

g.show_go_screen()

while g.running:
    g.new()
    g.show_go_screen()