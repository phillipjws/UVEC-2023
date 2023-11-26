# THIS IS MAIN

import sys
import pygame

from characters.thunder_the_viking import Thunder 
from characters.george_the_peacock import George


def main():
    # Initialize Pygame
    pygame.init()

    # Set the window size
    window_size = (600, 600)

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
                    player.move_left(window)
                elif event.key == pygame.K_RIGHT:
                    player.move_right(window)
                elif event.key == pygame.K_UP:
                    player.move_up(window)
                elif event.key == pygame.K_DOWN:
                    player.move_down(window)
        
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
