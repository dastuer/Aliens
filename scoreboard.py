import pygame.font
from ship import Ship
from pygame.sprite import Group


class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.hp_image = pygame.image.load('images/hp.bmp')
        self.hp_rect = self.hp_image.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 40)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        score_str = "Score: " + str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "Record: {:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def show_hp(self):
        for ship_num in range(self.stats.ship_left):
            self.hp_rect.x = 10 + ship_num * (self.hp_rect.width + 10)
            self.hp_rect.y = 0
            self.screen.blit(self.hp_image, self.hp_rect)
        

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # self.ships.hp_rect.draw(self.screen)
        self.screen.blit(self.high_score_image, self.high_score_rect)
            

