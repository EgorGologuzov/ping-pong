import pygame.time as tm


class Clock:
    def __init__(self, timing):
        self.past_reset = tm.get_ticks()
        self.timing = timing

    def reset(self):
        self.past_reset = tm.get_ticks()

    def time_has_come(self):
        if tm.get_ticks() - self.past_reset > self.timing:
            self.reset()
            return True
        return False

