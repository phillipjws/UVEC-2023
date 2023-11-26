import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        red = (205,102,29)

        self.image = pygame.Surface((30, 30))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y