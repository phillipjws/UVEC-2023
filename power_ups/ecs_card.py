import pygame

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, position, image_path):
        super(PowerUp, self).__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def apply_effect(self, character):
        pass

class EcsCard(PowerUp):
    def __init__(self, x, y):
        self.position = (x, y)
        super(EcsCard, self).__init__(self.position, "images/ecs_card_image.png")

    def apply_effect(self, character):
        pass  # TODO: need to add a field so they can win the level
