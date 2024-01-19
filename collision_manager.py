import pygame

class CollisionManager():
    def __init__(self, obj1, obj2):
        self.rect1 = obj1.rect
        self.rect2 = obj2.rect
    
    def check(self):
        if self.rect1.colliderect(self.rect2):
            return True