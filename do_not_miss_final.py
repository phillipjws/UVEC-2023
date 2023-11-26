# THIS IS MAIN
import pygame
import sys
import scenes
from characters.thunder_the_viking import Thunder 
from characters.george_the_peacock import George

frame = 50
clock = pygame.time.Clock()

class DoNotMissFinal():

    def __init__(self):
        pygame.init()

        # Create a player sprite
        self.player = Thunder(290, 60, 0, 0)
        self.player2 = George(290, 290, 0, 0)

        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Don't let Thunder miss the final!")
        self.clock = pygame.time.Clock()
        self.running_scene = scenes.starting_scene()
 
    def control(self, event, press):
        x_out = event.type == pygame.QUIT
        quit = press[pygame.K_q]
         
        # if anyone click on the cross
        # button or press the 'q' button 
        # it will quit the window
        return x_out or (quit)
 
    def run(self):
        while self.running_scene is not None:
            # Handle events
            eve = []
            press = pygame.key.get_pressed()
            for event in pygame.event.get():
                # if self.control(event, press):
                #     self.running_scene.terminate()
                # else:
                #     eve.append(event)
                # Handle quitting the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Handle keyboard input for player movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right()
                    elif event.key == pygame.K_UP:
                        self.player.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.player.move_down()
                    elif event.key == pygame.K_a:
                        self.player2.move_left()
                    elif event.key == pygame.K_d:
                        self.player2.move_right()
                    elif event.key == pygame.K_w:
                        self.player2.move_up()
                    elif event.key == pygame.K_s:
                        self.player2.move_down()

            # Update the player sprite
            self.player.update()
            self.player2.update()

            # Manage scene
            self.running_scene.process_input(eve, press)
            self.running_scene.update()

            # Clear the screen
            self.screen.fill((0, 0, 0))  # Clear the screen with black color

            # Rendering the scene
            self.running_scene.rendering()

            # Draw the player sprites
            self.screen.blit(self.player.image, self.player.position)
            self.screen.blit(self.player2.image, self.player2.position)

            # Update the display
            pygame.display.flip()

            # Tick the clock
            clock.tick(frame)


# main (our code will run from here)
if __name__ == "__main__":
    let_check = DoNotMissFinal()
    let_check.run()
    pygame.quit()