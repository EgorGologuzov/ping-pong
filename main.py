import pygame as pg
from ball import Ball
from platform import Platform
from AI import AI
from counter import Counter


class PingPong:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((600, 450))
        self.root = pg.Surface((600, 400))
        pg.display.set_caption('Ping Pong')
        pg.display.set_icon(pg.image.load('Sprites/ball.png'))
        self.player_platform, self.comp_platform = Platform(self, [575, 0]), Platform(self, [0, 0])
        self.ball = Ball(self)
        self.AI = AI(self)
        self.counter = Counter(self)
        self.objects = [self.ball, self.player_platform, self.comp_platform, self.AI, self.counter]
        self.clock = pg.time.Clock()
        self.main()

    def new_game(self):
        self.player_platform, self.comp_platform = Platform(self, [575, 0]), Platform(self, [0, 0])
        self.ball = Ball(self)
        self.AI = AI(self)
        # self.counter = Counter(self)
        self.objects = [self.ball, self.player_platform, self.comp_platform, self.AI, self.counter]
        self.clock = pg.time.Clock()

    def main(self):
        run = True
        while run:
            self.screen.fill((255, 255, 255), (0, 0, 600, 50))
            self.root.fill((0, 0, 0))
            self.clock.tick(60)
            # запуск main() у всех объектов
            for obj in self.objects:
                obj.main()
            # обработка событий
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        run = False
                        break

            if pg.key.get_pressed()[pg.K_DOWN]:
                self.player_platform.change_direction('DOWN')
            elif pg.key.get_pressed()[pg.K_UP]:
                self.player_platform.change_direction('UP')
            else:
                self.player_platform.change_direction('STOP')

            self.screen.blit(self.root, (0, 50))
            pg.display.update()


if __name__ == '__main__':
    PingPong()

