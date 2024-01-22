import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            "shoot": pygame.mixer.Sound("Audio/shoot.wav"),
            "explosion": pygame.mixer.Sound("Audio/explosion.wav"),
        }

    def PlaySound(self, sound):
        if sound in self.sounds:
            self.sounds[sound].play()

    def SetMusic(self, file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
