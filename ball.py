from object import *
import random as random


class Ball(Object):
    def __init__(self, app):
        self.app = app
        self.pos = [270, 200]
        self.image = pg.image.load('Sprites/ball.png')
        self.vector = random.choice([[8, 8], [-8, -8], [8, -8], [-8, 8]])
        self.size = self.image.get_size()
        self.clock = Clock(1)

    def main(self):
        self.draw()
        self.collision(self.app.player_platform, self.app.comp_platform)
        if self.clock.time_has_come():
            self.move()

    def collision(self, pl1, pl2):
        if self.vector[0] == 8:
            x, y1, y2 = pl1.pos[0], pl1.pos[1], pl1.pos[1] + pl1.size[1]
            bx, by1, by2 = self.pos[0] + self.size[0], self.pos[1], self.pos[1] + self.size[1]
            if bx >= x:
                if (y1 <= by1 <= y2) or (y1 <= by2 <= y2):
                    self.vector[0] = -8
        else:
            x, y1, y2 = pl2.pos[0] + self.size[0], pl2.pos[1], pl2.pos[1] + pl2.size[1]
            bx, by1, by2 = self.pos[0], self.pos[1], self.pos[1] + self.size[1]
            if bx <= x:
                if (y1 <= by1 <= y2) or (y1 <= by2 <= y2):
                    self.vector[0] = 8

        if self.pos[0] == 0:
            self.app.counter.counting(0)
            self.app.new_game()
        elif self.pos[0] + self.size[0] == self.app.root.get_size()[0]:
            self.app.counter.counting(1)
            self.app.new_game()



