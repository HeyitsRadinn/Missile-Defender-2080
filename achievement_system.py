import pygame, time

# change value to final screen size or import from main game file
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

class AchievementSystem():
    def __init__(self):
        self.font = pygame.font.SysFont('arial bold', 75)
        self.uncompleted_achievements = ['example_1', 'example_2', 'example_3'] # insert achievement names here
        self.completed_achievements = []
        self.time_since_last_pop_up = 0
    
    def complete(self, achievement):
        # achievement is an achievement name string
        self.uncompleted_achievements.remove(achievement)
        self.completed_achievements.append(achievement)
    
    def pop_up(self, achievement):
        # displays pop up
        self.text = self.font.render(f'congrats you completed the {achievement} achievement', True, (255,255,255))
        screen.blit(self.text, (10, 10))

    def checks(self):
        # insert achievement checks here
        if 'lol' == 'lol': # achievement criteria
            if 'example_1' in self.uncompleted_achievements:
                self.time_since_last_pop_up = time.time()
                self.complete('example_1')
            if time.time() - self.time_since_last_pop_up < 3:
                self.pop_up('example_1')