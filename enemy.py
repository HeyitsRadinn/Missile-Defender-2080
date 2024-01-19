import pygame

# change value to final screen size or import from main game file
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

class Enemy():
    def __init__(self, x, y, health, img, x_vel, y_vel):
        self.health = health
        self.image = img
        self.rect = self.image.get_rect(center=(x,y))
        self.velocity = pygame.Vector2(x_vel, y_vel)
    
    def move(self):
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.velocity[0] *= -1
        if self.rect.bottom > SCREEN_HEIGHT or self.rect.top < 0:
            self.velocity[1] *= -1
        self.rect.move_ip(self.velocity)
        
    def draw(self):
        screen.blit(self.image, self.rect)