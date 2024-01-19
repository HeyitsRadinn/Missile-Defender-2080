

import pygame, math, random, sys
from pygame.locals import *
from sys import exit
pygame.init()

screen = pygame.display.set_mode((1024, 765), 0, 32)

class ScreenTransition:
    def __init__ (self, colour, bg):
        # Pre: Takes colour of the background and the screen you want to transition to
        # Post: Stores the values for further use
        self.colour = colour # colour of the backgroudn transformation
        self.bg = bg # screen you're transitioning to

    def fadeout(self): 
        # Pre: Takes colour value and the amoutn of time for the transition
        # Post: Fades the screen to the set colour
        fade = pygame.Surface((1000, 800))
        fade.fill(self.colour)
        for alpha in range(0, 75): # how long after the fade before the next screen
            fade.set_alpha(alpha)
            screen.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(20) # speed of the fade - higher number is longer fade

    def fadein(self, bg): 
        # Pre: Takes the screen you want to transition to and amounf of time
        # Post: Transitions from the fadeout to fade in
        fade = pygame.Surface((1000, 800))
        fade.fill(self.colour)
        for alpha in range(0, 75): # how long after the fade before the next screen
            fade.set_alpha(75-alpha)
            screen.blit(fade, (0,0))
            bg()
            pygame.display.update()
            pygame.time.delay(50) # speed of the fade - higher number is longer fade
