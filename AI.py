

class AI:
    def __init__(self, app):
        self.app = app

    def main(self):
        platform_madian = round(self.app.comp_platform.pos[1] + self.app.comp_platform.size[1] / 2)
        by = round(self.app.ball.pos[1] + self.app.ball.size[1] / 2)
        if by >= platform_madian:
            self.app.comp_platform.change_direction('DOWN')
        else:
            self.app.comp_platform.change_direction('UP')

