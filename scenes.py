import pygame
import wall

pygame.init()

title_py = "Get to the Calc 1 final on time!"
frame = 50
WINDOWWIDTH, WINDOWHEIGHT = 600, 600

green = (69, 139, 116)
white = (255, 255, 255)
font_size = None

screen = pygame.display.set_mode([740, 340])
pygame.display.set_caption(title_py)

screen_font = pygame.font.Font(font_size, 50)

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

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
        self.screen = DISPLAYSURF 

        # make border blocks
        self.wallList = []

        for i in range(60, 570, 30):
            self.wallList.append(wall.Wall(30, i))
            self.wallList.append(wall.Wall(540, i))

        for i in range(60, 540, 30):
            if (i != 300 and i != 270) :
                self.wallList.append(wall.Wall(i, 540))
                self.wallList.append(wall.Wall(i, 60))

        for i in range(240, 390, 30):
            self.wallList.append(wall.Wall(210, i))
            self.wallList.append(wall.Wall(360, i))

        self.wallList.append(wall.Wall(240, 360))
        self.wallList.append(wall.Wall(330, 360))

        self.wallList.append(wall.Wall(240, 240))
        self.wallList.append(wall.Wall(330, 240))

        for i in range(150, 480, 30):
            if (i != 270 and i != 300) :
                self.wallList.append(wall.Wall(120, i))
                self.wallList.append(wall.Wall(450, i))

        for i in range(150, 450, 30):
            self.wallList.append(wall.Wall(i, 450))
            self.wallList.append(wall.Wall(i, 150))
        
        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(*self.wallList)
 
    def process_input(self, events, press):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = EndScene()
 
    def rendering(self):

        self.screen.fill(green)
        text = screen_font.render(title_py, 1, white)
        rect = text.get_rect()
        rect.centerx = 600 // 2
        rect.centery = 30

        self.screen.blit(text, rect)
        self.allsprites.draw(self.screen)
 
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
        text = screen_font.render("Thunder wins ", 1, white)
        rect = text.get_rect()
        rect.centerx = 300  # location from x-axis
        rect.centery = 50  # location from y-axis
        screen.blit(text, rect)

class HitPeacockScene(Scene):
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
        text = screen_font.render("George Wins ", 1, white)
        rect = text.get_rect()
        rect.centerx = 300  # location from x-axis
        rect.centery = 50  # location from y-axis
        screen.blit(text, rect)
 