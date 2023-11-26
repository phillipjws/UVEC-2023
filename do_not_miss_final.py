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
        self.player = Thunder(0, 240, 0, 0)
        self.player2 = George(320, 240, 0, 0)
        self.all_sprites = pygame.sprite.Group(self.player, self.player2)

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
        while self.running_scene != None:
            eve = []
            press = pygame.key.get_pressed()
            for event in pygame.event.get():
                if self.control(event, press):
                    self.running_scene.terminate()
                else:
                    eve.append(event)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left(self.screen)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right(self.screen)
                    elif event.key == pygame.K_UP:
                        self.player.move_up(self.screen)
                    elif event.key == pygame.K_DOWN:
                        self.player.move_down(self.screen)

                    elif event.key == pygame.K_a:
                        self.player2.move_left(self.screen)
                    elif event.key == pygame.K_d:
                        self.player2.move_right(self.screen)
                    elif event.key == pygame.K_w:
                        self.player2.move_up(self.screen)
                    elif event.key == pygame.K_s:
                        self.player2.move_down(self.screen)
            
            # Update the player sprite
            self.player.update()
            self.player2.update()

            if pygame.sprite.spritecollide(self.player, self.all_sprites, False):
                print("Sprites are touching!")
 
            # Manage scene
            self.running_scene.process_input(eve, press)
            self.running_scene.update()
             
            # dont move it as first we need to update then render
            self.running_scene.rendering()
             
            # moving the scene one by one
            self.running_scene = self.running_scene.next_scene  
             
            # means it will allow user to change the scene
            pygame.display.flip() 
            # Update and tick
            clock.tick(frame)

# main (our code will run from here)
if __name__ == "__main__":
    let_check = DoNotMissFinal()
    let_check.run()
    pygame.quit()