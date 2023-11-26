import pygame


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, position, image_path):
        super(PowerUp, self).__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def apply_affect(self, character):
        pass
