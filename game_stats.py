from os import write


class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
    
    def get_high_score(self):
        with open('record') as rec:
            mark = rec.read()
            self.high_score = int(mark)
            rec.close
    
    def write_high_score(self):
        with open('record', 'w') as rec:
            rec.write(str(self.high_score))
            rec.close

