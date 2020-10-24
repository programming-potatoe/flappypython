import pygame
import bird
import pipe
import random


class Game:
    def __init__(self):
        pygame.init()
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.image = pygame.transform.scale(pygame.image.load("assets/background.png"), (self.width, self.height))
        self.bird = bird.Bird(50, 50)
        self.pipes = []
        self.a = pipe.Pipe(self.win, 100, 0)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        time_since_last_call = 0

        # create first pipe
        self.pipes.append(pipe.Pipe(self.win, self.width, random.randint(0, 500) - 250))

        while run:
            dt = clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # print the background
            self.draw()

            time_since_last_call += dt

            # do we have to create a new pipe?
            if time_since_last_call > 5500:
                self.pipes.append(pipe.Pipe(self.win, self.width, random.randint(0, 500) - 250))
                time_since_last_call = 0

            # move or remove pipes
            for singlepipe in self.pipes:
                singlepipe.move_left()
                if singlepipe.out_of_frame():
                    self.pipes.remove(singlepipe)
                else:
                    singlepipe.draw()

            # print the bird
            self.bird.draw(self.win)

            pygame.display.update()

    pygame.quit()

    def draw(self):
        self.win.blit(self.image, (0, 0))


g = Game()
g.run()
