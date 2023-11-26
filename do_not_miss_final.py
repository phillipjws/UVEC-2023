# THIS IS MAIN

import sys
import pygame 

from characters.thunder_the_viking import Thunder 


def main():
    # Initialize Pygame
    pygame.init()

    # Set the window size
    window_size = (640, 480)

    # Create a window
    window = pygame.display.set_mode(window_size)

    # Create a player sprite
    player = Thunder(320, 240, 0, 0)


    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
        
        # Update the player sprite
        player.update()
        
        # Clear the window
        window.fill((255, 255, 255))
        
        # Draw the player sprite
        player.draw(window)
        
        # Update the display
        pygame.display.update()

   


if __name__ == '__main__':
    main()
