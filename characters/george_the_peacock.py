import pygame


class George(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)
        self.image= pygame.image.load('./characters/peacock.png')
        self.rect = self.image.get_rect(topleft = (x,y))
        

    
    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
    
    def draw(self, surface):
        surface.blit(self.image, self.position)
            
            
    def move_left(self):
        self.position = (self.position[0] -15 , self.position[1])
        self.image= pygame.image.load('./characters/peacock.png')
        
    
    def move_right(self):
        self.position = (self.position[0] +15, self.position[1])
        self.image = pygame.image.load('./characters/peacock-flip.png')

    def move_up(self):
        self.position = (self.position[0] , self.position[1] -15)
        
    
    def move_down(self):
        self.position = (self.position[0], self.position[1] +15)
