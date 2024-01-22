import pygame
import random

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, PowerUpType):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect(center=(x, y))
        self.type = PowerUpType
        self.duration = 5000

    def ApplyEffect(self, player):
        if self.type == "speed":
            player.increase_speed()

    def RemoveEffect(self, player):
        if self.type == "speed":
            player.reset_speed()
