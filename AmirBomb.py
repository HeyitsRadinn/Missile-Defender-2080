import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Missile Defender Game")


class Bomb:
    def __init__(self):
        self.x = random.randint(0, width)  # Initial x-coordinate (random)
        self.y = 0  # Start from the top of the screen
        self.target_x = random.randint(0, width)  # Random target x-coordinate
        self.target_y = height - 50  # Random target y-coordinate (considering city height)
        self.speed = 5  # Speed of the bomb

    def move(self):
        angle = math.atan2(self.target_y - self.y, self.target_x - self.x)
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)

    def draw(self):
        angle = math.degrees(math.atan2(self.target_y - self.y, self.target_x - self.x))
        line_length = 50
        end_x = self.x + line_length * math.cos(math.radians(angle))
        end_y = self.y + line_length * math.sin(math.radians(angle))
        pygame.draw.line(screen, (255, 0, 0), (self.x, self.y), (end_x, end_y), 5)

# Main game loop
clock = pygame.time.Clock()
bombs = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create a new bomb randomly with some probability
    if random.random() < 0.02:
        bombs.append(Bomb())

    # Update and draw bombs
    for bomb in bombs:
        bomb.move()
        bomb.draw()

    pygame.display.flip()
    screen.fill((0, 0, 0))  # Clear the screen

    clock.tick(30)  # Set the frame rate

pygame.quit()


##############################################################

import pygame
import sys

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.title = self.font.render("Missile Defender", True, (255, 255, 255))
        self.start_button = pygame.Rect(300, 200, 200, 50)  # Adjust position and size
        self.settings_button = pygame.Rect(300, 300, 200, 50)  # Adjust position and size
        self.leaderboard_button = pygame.Rect(300, 400, 200, 50)  # Adjust position and size
        self.exit_button = pygame.Rect(300, 500, 200, 50)  # Adjust position and size

    def draw_menu(self):
        self.screen.fill((0, 0, 0))  # Black background
        self.screen.blit(self.title, (250, 100))  # Adjust title position

        pygame.draw.rect(self.screen, (0, 128, 255), self.start_button)
        pygame.draw.rect(self.screen, (0, 128, 255), self.settings_button)
        pygame.draw.rect(self.screen, (0, 128, 255), self.leaderboard_button)
        pygame.draw.rect(self.screen, (0, 128, 255), self.exit_button)

        start_text = self.font.render("Start Game", True, (255, 255, 255))
        settings_text = self.font.render("Settings", True, (255, 255, 255))
        leaderboard_text = self.font.render("Leaderboard", True, (255, 255, 255))
        exit_text = self.font.render("Exit", True, (255, 255, 255))

        self.screen.blit(start_text, (325, 215))  # Adjust text position
        self.screen.blit(settings_text, (330, 315))  # Adjust text position
        self.screen.blit(leaderboard_text, (315, 415))  # Adjust text position
        self.screen.blit(exit_text, (350, 515))  # Adjust text position

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Missile Defender")

# Create an instance of MainMenu
settings = MainMenu(screen)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if settings.start_button.collidepoint(event.pos):
                print("Start Game")
                # Add code to start the game
            elif settings.settings_button.collidepoint(event.pos):
                print("Settings")
                # Add code to open settings
            elif settings.leaderboard_button.collidepoint(event.pos):
                print("Leaderboard")
                # Add code to show leaderboards
            elif settings.exit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    # Draw the main menu
    settings.draw_menu()

    # Update the display
    pygame.display.flip()
