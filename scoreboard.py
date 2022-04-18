import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        #Showing gthe number of ships available
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def check_high_score(self):
        #This is to check if there is a new high score
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def multi_render(self, line_array, x, y):
        rendered = []
        self.font = pgf.SysFont("Times", 48)

        for line in line_array:
            rendered.append(self.font.render(line, True, self.text_color, self.settings.bg_color))

        posY = self.score_rect.top + 100

        for i in range(len(rendered)):
            render_rect = (x, y + 60 * i)
            self.screen.blit(rendered[i], render_rect)

    def draw_instructions(self):
        #This will help display Instructions
        self.make_title("Instructions")

        instructions = ["Welcome to Alien Invasion",
                        "Move the ship by pressing the left and right arrow keys.",
                        "Press the spacebar to shoot bullets at the aliens.",
                        "Press enter when a level is finished to continue",
                        "to the next level.",
                        "You lose a life if an alien touches your ship, or passes you."
                        "If you lose 3 lives, the game is over.",
                        "Press backspace to return to the menu."]

        self.multi_render(instructions, self.screen_rect.centerx - 500, self.score_rect.top + 100)

    def make_title(self, msg):
        #Creates make_title
        self.font = pgf.SysFont("Times", 60, True)
        self.score_title = self.font.render(msg, True, self.text_colour, self.settings.bg_colour)

        self.score_title_rect = self.score_title.get_rect()
        self.score_title_rect.x = self.screen_rect.centerx - 150
        self.score_title_rect.y = self.screen_rect.top + 50

        self.screen.blit(self.score_title, self.score_title_rect)

    def draw_high_scores(self):
        #This will display high scores
        self.make_title('High Scores')
        scores_dict = {}
        scores_array = []

        try:
            with open(self.stats.my_scores, "r") as f:
                scores_dict = json.load(f)
        except FileNotFoundError:
            self.stats.create_high_score_json()

        for key, value in scores_dict.items():
            scores_array.append(f"{key}: {value}")

        self.multi_render(scores_array, self.screen_rect.centerx - 100, self.score_rect_top + 100)
