import pygame
import bird
import pipe
import random

state_start_screen = 0
state_start_game = 1
state_after_game = 2

class Game:
    def __init__(self):
        pygame.init()
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.image = pygame.transform.scale(pygame.image.load("assets/background.png"), (self.width, self.height))
        self.bird = None
        self.pipes = []
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.score = 0
        self.state = state_start_screen

    def run(self):
        """
        The main loop for running the game
        :return: none
        """
        run = True
        clock = pygame.time.Clock()
        new_pipe_timer = 0
        next_animation_timer = 0

        while run:
            if self.state == state_start_screen:

                # start background
                self.draw()

                # print the headline
                first_line = self.font.render('Welcome to the super cool FlappyPython', False, (255, 255, 255))
                self.win.blit(first_line, (round((self.win.get_width()/2)-(first_line.get_rect().width/2)), 50))

                # print the start button
                pygame.draw.rect(self.win, (0, 0, 255), (round((self.win.get_width()/2))-150, 300, 300, 100))

                # print the button text
                button_text = self.font.render('Start', False, (255, 255, 255))
                self.win.blit(button_text, (round((self.win.get_width()/2)-(button_text.get_rect().width/2)), 325))

                # event loop
                for event in pygame.event.get():
                    # exit actions
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        run = False

                    # check button click
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if round((self.win.get_width()/2))-150 <= pos[0] <= round((self.win.get_width()/2))+150 and 300 <= pos[1] <= 400:
                            self.state = state_start_game

                    # additionally we can progress with space
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.state = state_start_game


                # display everything
                pygame.display.update()

            elif self.state == state_start_game:
                game_is_running = True
                self.bird = bird.Bird(self.win, 50, round(self.win.get_height()/2))
                self.score = 0

                # delete previous pipes
                self.pipes = []

                while game_is_running:

                    # check for collision of bird with pipes
                    if self.bird.is_colliding(self.pipes):
                        game_is_running = False
                        self.state = state_after_game

                    # set up the game clock
                    dt = clock.tick(60)

                    # print the background
                    self.draw()

                    # set up timers
                    new_pipe_timer += dt
                    next_animation_timer += dt

                    if new_pipe_timer > 1500:
                        self.pipes.append(self.create_new_pipe())
                        new_pipe_timer = 0

                    # move pipes and check for border collisions
                    for singlepipe in self.pipes:
                        singlepipe.move_left()
                        if singlepipe.out_of_frame():
                            self.pipes.remove(singlepipe)
                            self.score += 1
                            del singlepipe
                        else:
                            singlepipe.draw()

                    # bird movement
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.bird.go_up()
                        if next_animation_timer > 250:
                            self.bird.next_animation()
                    else:
                        self.bird.go_down()
                        next_animation_timer = 0

                    # print the bird
                    self.bird.draw()

                    # print the score
                    score_message = self.font.render('Score: ' + str(self.score), False, (255, 0, 0))
                    self.win.blit(score_message, (0, 0))

                    # event loop
                    for event in pygame.event.get():

                        # exit options
                        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            game_is_running = False
                            run = False


                    # display everything
                    pygame.display.update()

            else: # self.state == end something

                # game is over, print an end message
                end_message = self.font.render('YOU FAILED!! Your score is: ' + str(self.score), False, (255, 0, 0))
                self.win.blit(end_message,
                              (round((self.win.get_width()/2)-(end_message.get_rect().width/2)),
                               round((self.win.get_height()/2)-(end_message.get_rect().height/2))))

                # print the menue button
                pygame.draw.rect(self.win, (0, 0, 255), (round((self.win.get_width()/2))-150, 400, 300, 100))

                # print the button text
                button_text = self.font.render('Back to menue', False, (255, 255, 255))
                self.win.blit(button_text, (round((self.win.get_width()/2)-(button_text.get_rect().width/2)), 425))

                # event loop
                for event in pygame.event.get():
                    # exit events
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        run = False
                    # button click event
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if round((self.win.get_width()/2))-150 <= pos[0] <= round((self.win.get_width()/2))+150 and 400 <= pos[1] <= 500:
                            self.state = state_start_screen

                    # additionally we can progress with space
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.state = state_start_screen

                # display everything
                pygame.display.update()

    pygame.quit()

    def draw(self):
        """
        Draws the game background
        :return: none
        """
        self.win.blit(self.image, (0, 0))

    def create_new_pipe(self):
        """
        Creates new pipe objects
        :return: pipe object
        """
        return pipe.Pipe(self.win, random.randint(150, self.height - 150))


g = Game()
g.run()
