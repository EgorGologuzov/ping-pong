import pygame as pg
from clock import Clock


class Object:
    def __init__(self, app):
        self.app = app
        self.pos = [0, 0]
        self.image: pg.Surface = None
        self.vector = [10, 10]
        self.size = self.image.get_size()
        self.clock = Clock(1)

    def main(self):
        self.draw()
        if self.clock.time_has_come():
            self.move()

    def draw(self):
        self.app.root.blit(self.image, self.pos)

    # по дефолту объект двигается по заданному вектору и отскакивает от границ окна
    def move(self):
        x1, y1 = self.pos[0] + self.vector[0], self.pos[1] + self.vector[1]
        x2, y2 = x1 + self.size[0], y1 + self.size[1]
        size_root = self.app.root.get_size()
        x_offset, y_offset = self.vector[0], self.vector[1]

        if x1 < 0:
            x_offset = self.vector[0] - x1
            self.vector[0] = -self.vector[0]
        elif x2 > size_root[0]:
            x_offset = self.vector[0] - x2 + size_root[0]
            self.vector[0] = -self.vector[0]
        if y1 < 0:
            y_offset = self.vector[1] - y1
            self.vector[1] = -self.vector[1]
        elif y2 > size_root[1]:
            y_offset = self.vector[1] - y2 + size_root[1]
            self.vector[1] = -self.vector[1]

        self.pos[0] += x_offset
        self.pos[1] += y_offset

