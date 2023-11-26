import pygame


class Thunder(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)
        self.image = pygame.image.load('./characters/thunder-standing.png')
        self.rect = self.image.get_rect(topleft = (x,y))
    
    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
    
    def draw(self, surface):
        surface.blit(self.image, self.position)
            
            
    def move_left(self, surface):
        self.position = (self.position[0] -15 , self.position[1])
        self.image = pygame.image.load('./characters/thunder-standing-flip.png')
        
    
    def move_right(self, surface):
        self.position = (self.position[0] +15, self.position[1])
        self.image = pygame.image.load('./characters/thunder-standing.png')

    def move_up(self, surface):
        self.position = (self.position[0] , self.position[1] -15)
        
    
    def move_down(self, surface):
        self.position = (self.position[0], self.position[1] +15)
        