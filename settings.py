class Settings:
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (255, 255,  255)

        self.ship_limit = 3

        self.fleet_drop_speed = 10
        self.bullets_allowed = 10
        self.speedup_scale = 1.1
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 4
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
