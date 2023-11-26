import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Call the parent's constructor
        #pygame.sprite.Sprite.__init__(self)
        super(Wall, self).__init__()

        #red = (205,102,29)

        # Hardcoded path to the image
        image_path = "images/wall (1).png" 

        # Load the image
        self.image = pygame.image.load(image_path).convert_alpha()

        # self.image = pygame.Surface((30, 30))
        # self.image.fill(red)
        self.rect = self.image.get_rect()
        # self.width = self.image.get_width()
        # self.height = self.image.get_height()
        # self.x = x
        # self.y = y

        self.rect = self.image.get_rect(topleft=(x, y))