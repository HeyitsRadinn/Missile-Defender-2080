import pygame
import sys

# Initialize Pygame
pygame.init()

Cities = pygame.image.load('assets\MissleDefenderCity.png').convert_alpha

# Constants
SCREENWIDTH, SCRENHEIGHT = 820, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# City class
class City(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.max_health = 100
        self.health = self.max_health
        self.ammo = 10

    def HealthUpdate(self):
        health_ratio = self.health / self.max_health
        bar_width = int(50 * health_ratio)
        health_bar = pygame.Surface((bar_width, 5))
        health_bar.fill((0, 255, 0))
        return health_bar


screen = pygame.display.set_mode((SCREENWIDTH, SCRENHEIGHT))
pygame.display.set_caption("Missile Defender")

# Create Cities
Cities = pygame.sprite.Group()
city_positions = [(125, 500), (300, 500), (475, 500), (650, 500)]

for pos in city_positions:
    city = City(*pos)
    Cities.add(city)

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for city in Cities:
                if city.rect.collidepoint(event.pos) and city.ammo > 0:
                    city.health -= 20
                    #city.ammo -= 1

    # Update city
    for city in Cities:
        health_bar = city.HealthUpdate()
        screen.blit(city.image, city.rect.topleft)
        screen.blit(health_bar, (city.rect.left, city.rect.bottom + 5))

        # Ammo
        font = pygame.font.Font(None, 20)
        ammo_text = font.render(f"Ammo: {city.ammo}", True, RED)
        screen.blit(ammo_text, (city.rect.left, city.rect.bottom + 20))

 
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)