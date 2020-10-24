import pygame


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.movement = 0  # 0 = down, 1 = up
        self.image = pygame.image.load("assets/bird.png").convert_alpha()

    def draw(self, win):
        """
        Draws the bird
        :param win: surface
        :return: None
        """
        win.blit(self.image, (self.x, self.y))

    def go_up(self):
        """
        Makes the bird go up
        :return: None
        """
        self.y -= 1

    def go_down(self):
        """
        Makes the bird go down
        :return: none
        """
        self.y += 1
