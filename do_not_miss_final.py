# THIS IS MAIN
import pygame
import level_one
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep

frame = 50
clock = pygame.time.Clock()



class DoNotMissFinal(ConnectionListener):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Don't let Thunder miss the final!")
        self.clock = pygame.time.Clock()
        self.running_scene = level_one.starting_scene()
        self.Connect(("134.87.42.233", 12345))
 
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
            connection.Pump()
            self.Pump()

# main (our code will run from here)
if __name__ == "__main__":
    let_check = DoNotMissFinal()
    let_check.run()
    pygame.quit()