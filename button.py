import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        self.msg = msg
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def prep_button_to_message(self):
        self.width, self.height = 400, 200
        self.text_colour = (255, 255, 255)
        self.button_colour = (0, 0, 0)
        self.font = pgf.SysFont(None, 80)

        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center


        self.prep_msg(self.msg)

    def _prep_button_to_title(self):
        # Properties of the message
        self.width, self.height = 800, 200
        self.text_colour = (0, 0, 0)
        self.button_colour = self.settings.bg_colour
        self.font = pgf.SysFont("Times", 100,True)

        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.screen_rect.centerx,self.screen_rect.centery//2)

        self.prep_msg(self.msg)

    def change_rect_to(self,x,y):
        self.rect.center = (x,y)
        self._prep_msg(self.msg)

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
