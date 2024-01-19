import pygame
import sys

# Initialize Pygame
pygame.init()

# Game settings
class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.sound_volume = 0.5
        self.controls = {'fire': pygame.K_SPACE, 'pause': pygame.K_p}

# User Interface
class UI:
    def __init__(self, settings):
        self.settings = settings
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption("Missile Defender")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.ammo = 10

    def update_score(self, points):
        self.score += points

    def update_ammo(self, ammo):
        self.ammo = ammo

    def draw_ui(self):
        self.screen.fill((255, 255, 255))  # White background
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        ammo_text = self.font.render(f"Ammo: {self.ammo}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(ammo_text, (10, 50))
        pygame.display.flip()

    def draw_pause_menu(self):
        pause_text = self.font.render("Paused", True, (255, 0, 0))
        self.screen.blit(pause_text, (self.settings.screen_width // 2 - 50, self.settings.screen_height // 2 - 25))
        pygame.display.flip()

# Initialize game settings and UI
game_settings = Settings()
game_ui = UI(game_settings)

# Main game loop
running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == game_settings.controls['pause']:
                paused = not paused

    if not paused:
        # Update game logic here (e.g., handle user input, update score, etc.)
        # For this example, we'll simulate score and ammo updates
        game_ui.update_score(1)
        game_ui.update_ammo(5)

        # Draw UI
        game_ui.draw_ui()
    else:
        # Draw pause menu
        game_ui.draw_pause_menu()

    game_ui.clock.tick(60)  # Cap the frame rate to 60 FPS

pygame.quit()
sys.exit()
