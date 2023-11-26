import pygame


class Thunder(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()
        self.character = "Thunder"
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)
        self.image = pygame.image.load('./characters/thunder-standing.png')
        
        
    
    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
    
    def draw(self, surface):
        surface.blit(self.image, self.position)
            
            
    def move_left(self):
        self.position = (self.position[0] -15 , self.position[1])
        self.image = pygame.image.load('./characters/thunder-standing-flip.png')
        
    
    def move_right(self):
        self.position = (self.position[0] +15, self.position[1])
        self.image = pygame.image.load('./characters/thunder-standing.png')

    def move_up(self):
        self.position = (self.position[0] , self.position[1] -15)
        
    
    def move_down(self):
        self.position = (self.position[0], self.position[1] +15)
        