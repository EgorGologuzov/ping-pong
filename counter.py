from object import Object
from clock import Clock
import pygame as pg


class Counter(Object):
    def __init__(self, app):
        self.app = app
        self.pos = [0, 0]
        self.vector = [0, 0]
        self.font = pg.font.SysFont(None, 40)
        self.count = [0, 0]
        self.image = self.font.render(f'{self.count[0]} : {self.count[1]}', True, (0, 0, 0))
        self.size = self.image.get_size()
        self.clock = Clock(10)

    def counting(self, player):
        if player:
            self.count[0] += 1
        else:
            self.count[1] += 1
        self.image = self.font.render(f'{self.count[0]} : {self.count[1]}', True, (0, 0, 0))
        self.size = self.image.get_size()

    def draw(self):
        self.app.screen.blit(self.image, self.image.get_rect(center=(300, 25)))


