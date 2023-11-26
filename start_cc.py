import pygame
import pygame.freetype

pygame.init()

title_py = "DO NOT MISS THE FINAL"
frame = 50

# Photos for button
start_photo = pygame.image.load('start_button1.png')
start_photo = pygame.transform.scale(start_photo, (150, 200))

background = pygame.image.load('buildings-eow.jpg')

thunder = pygame.image.load('victor.png')
thunder = pygame.transform.scale(thunder, (200, 200))

peacock = pygame.image.load('peacock.png')
peacock = pygame.transform.scale(peacock, (200, 200))

green = (69, 139, 116)
white = (255, 255, 255)
font_size = None

screen = pygame.display.set_mode([740, 340])
pygame.display.set_caption(title_py)

screen_font = pygame.font.Font(font_size, 60)

class Button():
    def __init__(self, image, x, y):
        self.img = image
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))


start_button = Button(start_photo, 100, 200)
thunder_button = Button(thunder, 300, 200)
peacock_button = Button(peacock, 100, 200)


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
            # New
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.next_scene = EndScene()
            # New

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = EndScene()

    def rendering(self):

        screen.fill(white)
        screen.blit(background, (0, 0))

        text = screen_font.render(title_py, 1, (0,0,0))
        rect = text.get_rect()
        rect.centerx = 600 // 2
        rect.centery = 50
        screen.blit(text, rect)

        start_button.draw()

    def update(self):
        pass


class EndScene(Scene):
    def __init__(self):
        super().__init__()

    def process_input(self, events, press):
        for event in events:
            # New
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.next_scene = starting_scene() ### HERE ADD NEW SCENE
            # New

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = starting_scene()

    def update(self):
        pass

    # rendering the scene function
    def rendering(self):
        screen.fill(green)

        # font color will be white
        text = screen_font.render("Your characters! ", 1, white)
        text2 = screen_font.render("George", 1, white)
        text3 = screen_font.render("Thunder", 1, white)

        rect = text.get_rect()
        rect2 = text2.get_rect()
        rect3 = text3.get_rect()

        rect.centerx = 300  # location from x-axis
        rect.centery = 50  # location from y-axis
        rect2.centerx = 200
        rect2.centery = 425
        rect3.centerx = 400
        rect3.centery = 425

        screen.blit(text, rect)  # places onto screen
        screen.blit(text2, rect2)
        screen.blit(text3, rect3)

        thunder_button.draw()
        peacock_button.draw()
