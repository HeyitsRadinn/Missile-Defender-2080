
import pygame

class Missile:
    def __init__(self, StartPosition, TargetPosition, speed):
        # Pre: Takes the starting position (x, y), target position (TargetX, TargetY), and speed.
        # Post: Initializes a Missile object with the specified attributes.
        self.x, self.y = StartPosition
        self.TargetX, self.TargetY = TargetPosition
        self.speed = speed
        self.size = 5
        self.colour = (255, 0, 0)
        self.active = True

    def MoveTowardsDestination(self):
        # Pre: None
        # Post: Moves the missile towards its target based on its current direction and speed.
        distance = ((self.TargetX - self.x) ** 2 + (self.TargetY - self.y) ** 2) ** 0.5

        if distance > 0:
            DirectionX = self.TargetX - self.x / distance
            DirectionY = self.TargetY - self.y / distance
            self.x += int(self.speed * DirectionX)
            self.y += int(self.speed * DirectionY)

    def CheckCollision(self, target):
        # Pre: Takes another object (target) and checks if a collision occurs.
        # Post: Returns True if a collision is detected and sets the missile to inactive, otherwise returns False.
        distance = ((target.x - self.x) ** 2 + (target.y - self.y) ** 2) ** 0.5
        if distance < self.size + target.size:
            self.active = False
            return True
        else:
            return False



    def draw(self, screen):
        # Pre: Takes a Pygame screen surface.
        # Post: Draws the missile on the screen as a circle with the specified color and size.
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)


