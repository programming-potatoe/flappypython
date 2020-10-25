import pygame


class Bird:
    def __init__(self, win,  x, y):
        self.win = win
        self.x = x
        self.y = y
        self.direction = 0  # 0 = down 1st, 1 = down 2nd, 3 = up 1st, 4 = up 2nd
        self.images = []
        self.images.append(pygame.image.load("assets/quad_bird.png").convert_alpha())
        self.images.append(pygame.image.load("assets/quad_bird2.png").convert_alpha())
        self.images.append(pygame.image.load("assets/quad_bird3.png").convert_alpha())
        self.images.append(pygame.image.load("assets/quad_bird4.png").convert_alpha())
        self.images.append(pygame.image.load("assets/quad_bird5.png").convert_alpha())
        self.images.append(pygame.image.load("assets/quad_bird6.png").convert_alpha())
        self.images.append(pygame.image.load("assets/quad_bird7.png").convert_alpha())
        self.images.append(pygame.image.load("assets/quad_bird8.png").convert_alpha())
        self.images.append(pygame.image.load("assets/quad_bird9.png").convert_alpha())
        self.images.append(pygame.image.load("assets/quad_bird10.png").convert_alpha())
        self.images.append(pygame.image.load("assets/quad_bird11.png").convert_alpha())
        self.images.append(pygame.image.load("assets/quad_bird12.png").convert_alpha())
        self.current_image = self.images[0]
        self.height = self.images[0].get_height()
        self.width = self.images[0].get_width()
        self.initial_step_size = 1
        self.step_size = self.initial_step_size
        self.max_step_size = 10

    def draw(self):
        """
        Draws the bird to the surface depending on the direction (up=animation, down = no animation)
        :return: None
        """
        if self.direction in (2, 3):
            self.win.blit(self.current_image, (self.x, self.y))
        else:
            self.win.blit(self.images[0], (self.x, self.y))

    def go_up(self):
        """
        Makes the bird go up, ups the step size the longer the bird goes in this direction
        :return: None
        """
        # check if we are already going up, we need to then up the step size, otherwise set it back to 1
        # since a +1 in every step is too much we only do it in every second
        if self.direction == 3:
            self.step_size += 1

            # we need to cap the maximum step_size
            if self.step_size > self.max_step_size:
                self.step_size = self.max_step_size

            self.direction = 4
        elif self.direction == 4:
            self.direction = 3
        else:
            self.direction = 3
            self.step_size = self.initial_step_size

        # make the step
        self.y -= self.step_size

        # check if the step brings us out of the frame
        if self.y <= 0:
            self.y = 0

    def go_down(self):
        """
        Makes the bird go down, ups the step size the longer the bird goes in this direction
        :return: none
        """
        # check if we are already going down, we need to then up the step size, otherwise set it back to 0
        # since a +1 in every step is too much we only do it in every second
        if self.direction == 0:
            self.step_size += 1

            # we need to cap the maximum step_size
            if self.step_size > self.max_step_size:
                self.step_size = self.max_step_size

            self.direction = 1
        elif self.direction == 1:
            self.direction = 0
        else:
            self.direction = 0
            self.step_size = self.initial_step_size

        # make the step
        self.y += self.step_size

        # check if the step brings us out of the frame
        if self.y >= (self.win.get_height() - self.height):
            self.y = self.win.get_height() - self.height

        # reset animation
        self.current_image = self.images[0]

    def is_colliding(self, pipes):
        """
        Checks if the bird is colliding with one of the pipes provided
        :param pipes: list of pipes
        :return: boolean
        """
        for pipe in pipes:
            # collision can only appear if bird is at same x coordinates as pipe
            if (self.x + self.width) >= pipe.x and self.x <= (pipe.x + pipe.width):
                # for a collision bird has to be outside the hole of the pipe
                if self.y <= (pipe.hole_position - (pipe.hole_size/2)) or (self.y + self.height) >= (pipe.hole_position + pipe.hole_size/2):
                    return True
        return False

    def next_animation(self):
        index = self.images.index(self.current_image)
        if index == 11:
            index = 0
        else:
            index += 1
        self.current_image = self.images[index]
