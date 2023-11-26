# THIS IS MAIN
import pygame
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep


class DoNotMissFinal(ConnectionListener):
    def __init__(self):
        pass
        pygame.init()
        width, height = 600, 600

        # initialize the screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Don't let Thunder miss the final!")

        # initialize pygame clock
        self.clock = pygame.time.Clock()
        self.Connect(("127.0.0.1", 12345))

    def update(self):
        connection.Pump()
        self.Pump()
        # sleep to make the game 60 fps
        self.clock.tick(60)

        # clear the screen
        self.screen.fill(0)

        for event in pygame.event.get():
            # quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()

        # update the screen
        pygame.display.flip()


if __name__ == "__main__":
    bg = DoNotMissFinal()  # __init__ is called right here
    while 1:
        bg.update()
