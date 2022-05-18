import pygame, random, os, neat


class Bird():
    def __init__(self):
        self.gravity = .075
        self.birdMovement = 0
        self.score = 0
        self.gameActive = True
        self.end = False
        self.deathSound = pygame.mixer.Sound('sound_sfx_hit.wav')

        # bird
        birdDownflap = pygame.image.load('yellowbird-downflap.png').convert_alpha()
        birdMidflap = pygame.image.load('yellowbird-midflap.png').convert_alpha()
        birdUpflap = pygame.image.load('yellowbird-upflap.png').convert_alpha()
        self.birdFrames = [birdDownflap, birdMidflap, birdUpflap]
        self.birdIndex = 0
        self.birdSurface = self.birdFrames[self.birdIndex]
        self.birdRect = self.birdSurface.get_rect(center=(50, random.randint(200, 400)))

    def checkCollision(self, pipes):
        for pipe in pipes:
            if self.birdRect.colliderect(pipe):  # checks if the bird rect is colliding with the pipe rect
                self.deathSound.play()
                return True

        if self.birdRect.top <= -100 or self.birdRect.bottom >= 450:
            return True

        return False

    def animateBird(self):
        newBird = self.birdFrames[self.birdIndex]
        newBirdRect = newBird.get_rect(center=(50,
                                               self.birdRect.centery))  # take the previous y of the current bird and creates the new one at the same location
        self.birdSurface, self.birdRect = newBird, newBirdRect

    def rotateBird(self):
        newBird = pygame.transform.rotozoom(self.birdSurface, self.birdMovement * -10,
                                            1)  # can scale and rotate a surface
        # (surface, rotation, scale)

        return newBird

    def animateTitleScreen(self):
        self.birdMovement = 0
        if self.birdRect.centery <= 270:
            self.gravity += .05
        if self.birdRect.centery >= 300:
            self.gravity -= .05

    def gameOverAnimate(self):
        return False

        self.birdMovement += self.gravity
        rotatedBird = self.rotateBird(self.birdSurface)
        screen.blit(rotatedBird, birdRect)
        self.birdRect.centery += self.birdMovement

        if self.birdRect.bottom >= 450:
            self.birdMovement = 0
            return False
        return True

    def jump(self):
        if self.gameActive:
            self.birdMovement = 0
            self.birdMovement -= 2.5
        else:
            self.birdRect.center = (50, random.randint(200, 400))
            self.birdMovement = 0
            self.score = 0


def main(genomes, config):
    def drawFloor():  # blits 2 floor surfaces right next to each other
        screen.blit(floorSurface, (floorX, 450))
        screen.blit(floorSurface, (floorX + 288, 450))

    def createPipe():
        randomPipePos = random.choice(pipeHeight)  # chooses random number out of the list
        bottomPipe = pipeSurface.get_rect(midtop=(350, randomPipePos))  # makes new bottom pipe moves from top
        topPipe = pipeSurface.get_rect(midbottom=(350, randomPipePos - 110))  # makes new top pipe moves from bottom

        return bottomPipe, topPipe

    def movePipes(pipes):
        for pipe in pipes:
            pipe.centerx -= 1
        return pipes

    def drawPipes(pipes):
        for pipe in pipes:
            if pipe.bottom >= 512:
                screen.blit(pipeSurface, pipe)
            else:
                flipPipe = pygame.transform.flip(pipeSurface, False, True)  # flips pipe (surface,flipX?,flipY?)
                screen.blit(flipPipe, pipe)

    pygame.init()
    screen = pygame.display.set_mode((288, 512))
    clock = pygame.time.Clock()  # creates clock object

    # title and icon
    pygame.display.set_caption('Flappy Bird')
    icon = pygame.image.load('FlappyIcon.ico')
    pygame.display.set_icon(icon)

    # background
    bgSurface = pygame.image.load('background-day.png').convert()  # day background; convert helps pygame run

    # base
    floorSurface = pygame.image.load('base.png').convert()
    floorX = 0

    BIRDFLAP = pygame.USEREVENT + 1  # + 1 so that it doesn't change the spawn pipe user event
    pygame.time.set_timer(BIRDFLAP, 200)

    # pipes
    pipeSurface = pygame.image.load('pipe-green.png')
    pipeList = []
    SPAWNPIPE = pygame.USEREVENT  # spawnpipe userevent to be triggered by timer
    pygame.time.set_timer(SPAWNPIPE, 1500)  # SPAWNPIPE triggered every 1.5 seconds
    pipeHeight = [i for i in range(200, 400)]  # possible pipe locations
    pipeList.extend(createPipe())

    nets = []
    ge = []
    birds = []

    for _, g in genomes:  # under score because genomes has tuples (index, genome object)
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird())
        g.fitness = 0
        ge.append(g)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            for bird in birds:
                if event.type == BIRDFLAP and bird.birdIndex < 2 and bird.end == False:  # every .2 seconds the bird image changes to create the animation
                    bird.birdIndex += 1
                elif bird.end == False:
                    bird.birdIndex = 0

                bird.animateBird()

            if event.type == SPAWNPIPE:  # runs each time SPAWNPIPE is triggered so every 1.2 seconds
                pipeList.extend(createPipe())
                for g in ge:
                    g.fitness += 5

        pipe_ind = 1  # pipe index
        if len(birds) > 0:
            if len(pipeList) > 1 and birds[0].birdRect.left > pipeList[0].right:
                pipe_ind = 3  # if pipe passed change the pipe to be the second pipe in the list
        else:  # if there is no birds left quit the game
            running = False
            break

        for i, bird in enumerate(birds):
            ge[i].fitness += 0.01  # this might be too much

            top_pipe, bottom_pipe = pipeList[pipe_ind], pipeList[pipe_ind-1]

            # holds output of the neural network
            output = nets[birds.index(bird)].activate((bird.birdRect.y,
                                                       top_pipe.bottom, # top pipe
                                                       bottom_pipe.top)) # bottom pipe

            if output[0] > 0.5:  # only want the first output neuron
                bird.jump()

        screen.blit(bgSurface, (0, 0))  # blits background

        drawPipes(pipeList)
        drawFloor()

        for i, bird in enumerate(birds):
            if bird.end == True:
                bird.end = bird.gameOverAnimate()  # animates falling bird and returns False when bird passes y 450
                if bird.gameActive:
                    screen.blit(rotatedBird, bird.birdRect)

            if any([b.gameActive for b in birds]):
                # bird movement
                bird.gravity = .075

                bird.birdMovement += bird.gravity  # gives bird gravity

                rotatedBird = bird.rotateBird()

                bird.birdRect.centery += bird.birdMovement  # gives bird's rectangle the same gravity
                # centery and centerx is the only way to move the rectangle
                if bird.gameActive:
                    screen.blit(rotatedBird, bird.birdRect)

                if bird.checkCollision(pipeList):
                    bird.gameActive = False
                    ge[i].fitness -= 1  # everytime a bird hits a pipe it will remove from its fitness
                    birds.pop(i)
                    nets.pop(i)
                    ge.pop(i)

        # pipe movement
        pipeList = movePipes(pipeList)

        # floor movement
        floorX -= .6
        if floorX <= -288:  # checks when floor is off-screen and teleports it back to start pos
            floorX = 0

        for i in range(len(pipeList)-1,-1,-1):
            if pipeList[i].centerx <= 0:
                pipeList.remove(pipeList[i])


        clock.tick(144)  # fps limit for game
        pygame.display.update()


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)  # loading in the config file

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)  # population based on what's in the config file

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)  # give the output to the console

    # Run for up to 50 generations.
    winner = p.run(main, 50)  # (fitness function, times to run fitness function)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
