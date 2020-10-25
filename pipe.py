import pygame


class Pipe:
    def __init__(self, win, hole_position):
        self.win = win
        self.hole_position = hole_position
        self.x = self.win.get_width()
        self.image_bot = pygame.image.load("assets/pipe.png")
        self.image_top = pygame.transform.flip(pygame.image.load("assets/pipe.png"), False, True)
        self.width = self.image_bot.get_width()
        self.height = self.image_bot.get_height()
        self.step_size = 5
        self.hole_size = 100

    def draw(self):
        """
        Draws the pipe
        :return: none
        """
        self.win.blit(self.image_top, (self.x, (self.hole_position - 1000 - (self.hole_size/2))))
        self.win.blit(self.image_bot, (self.x, (self.hole_size/2) + self.hole_position))

    def move_left(self):
        """
        Moves the pipe to the left
        :return:
        """
        self.x = self.x - self.step_size

    def out_of_frame(self):
        """
        Tests if the pipe is out of the left frame
        :return: boolean
        """
        if self.x < (0 - self.width):
            return True
        return False
