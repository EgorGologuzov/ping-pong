from object import *


class Platform(Object):
    def __init__(self, app, pos: list[int, int]):
        self.app = app
        self.image = pg.image.load('Sprites/platform.png')
        self.pos = pos
        self.vector = [0, 0]
        self.size = self.image.get_size()
        # self.side = side
        self.clock = Clock(10)

    def change_direction(self, direction=None):
        if direction is None:
            if self.vector[1] == 5:
                self.vector[1] = -5
            elif self.vector[1] == -5:
                self.vector[1] = 5
        elif direction == 'UP':
            self.vector[1] = -5
        elif direction == 'DOWN':
            self.vector[1] = 5
        elif direction == 'STOP':
            self.vector[1] = 0


