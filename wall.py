import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Call the parent's constructor
        super(Wall, self).__init__()

        # Hardcoded path to the image
        image_path = "images/wall (1).png" 

        # Load the image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))