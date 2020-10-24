import pygame


class Pipe:
    def __init__(self, win, x, hole_position):
        self.hole_position = hole_position
        self.x = x
        self.image_bot = pygame.image.load("assets/pipe.png")
        self.image_top = pygame.transform.flip(pygame.image.load("assets/pipe.png"), False, True)
        self.win = win


    def draw(self):
        """
        Draws the pipe
        :return: none
        """
        self.win.blit(self.image_top, (self.x, (self.win.get_height()/2-1075) + self.hole_position))
        self.win.blit(self.image_bot, (self.x, self.win.get_height()/2 + self.hole_position))

    def move_left(self):
        self.x = self.x - 1

    def out_of_frame(self):
        if self.x < 0:
            return True
        return False
