import pygame
import wall

pygame.init()

title_py = "Level 1: Get to the Calc 1 final on time!"
frame = 50

green = (69, 139, 116)
white = (255, 255, 255)
font_size = None

screen = pygame.display.set_mode([740, 340])
pygame.display.set_caption(title_py)

screen_font = pygame.font.Font(font_size, 50)

# scene class in pygame
class Scene():
    def __init__(self):
        self.next_scene = self
 
    def process_input(self, events, press):
        raise NotImplementedError
 
    def update(self):
        raise NotImplementedError
 
    def rendering(self):
        raise NotImplementedError
 
    def terminate(self):
        self.next_scene = None

# this will be the first scene class as
# the prime and opening scene of our app
class starting_scene(Scene):
    def __init__(self):
        super().__init__()
        self.screen = screen
 
    def process_input(self, events, press):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = EndScene()
 
    def rendering(self):

        wallList = [
            wall.Wall(70, 100),
            wall.Wall(100, 100),
            wall.Wall(130, 100),
            wall.Wall(160, 100),
            wall.Wall(190, 100),
            wall.Wall(220, 100)
            ]
        
        allsprites = pygame.sprite.Group()
        allsprites.add(wallList)

        self.screen.fill(green)
        text = screen_font.render(title_py, 1, white)
        rect = text.get_rect()
        rect.centerx = 600 // 2
        rect.centery = 50
        screen.blit(text, rect)
 
    def update(self):
        pass

class EndScene(Scene):
    def __init__(self):
        super().__init__()
 
    def process_input(self, events, press):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = starting_scene()
 
    def update(self):
        pass
    # rendering the scene function
    def rendering(self):
        screen.fill(green)
         
        # font color will be white
        text = screen_font.render("Scene 2 Game Ending ", 1, white)
        rect = text.get_rect()
        rect.centerx = 300  # location from x-axis
        rect.centery = 50  # location from y-axis
        screen.blit(text, rect)
 