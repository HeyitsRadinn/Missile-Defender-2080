import pygame
import random

class Particle:
    def __init__(self, x, y, lifespan):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
        self.color = (255, random.randint(0, 100), 0)  # Orange-red
        self.lifespan = lifespan
        self.velocity = [random.uniform(-1, 1), random.uniform(-3, 0)]

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.size = max(self.size - 0.1, 0)
        self.lifespan -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

class ExplosionEffect:
    def __init__(self, position, use_sprites=False):
        self.position = position
        self.use_sprites = use_sprites
        self.particles = []
        self.sprites = []
        self.done = False

        if use_sprites:
            self.load_sprites()
            self.current_frame = 0
        else:
            self.create_particles()

    def load_sprites(self):
        # Load your explosion sprites here
        self.sprites = [pygame.image.load('explosion1.png'), pygame.image.load('explosion2.png')]  # etc.
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def create_particles(self, particle_count=50):
        for _ in range(particle_count):
            self.particles.append(Particle(self.position[0], self.position[1], random.randint(20, 50)))

    def update(self):
        if self.use_sprites:
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.current_frame += 1
                if self.current_frame == len(self.sprites):
                    self.done = True
                    return
        else:
            for particle in self.particles[:]:
                particle.update()
                if particle.lifespan <= 0 or particle.size <= 0:
                    self.particles.remove(particle)
            if not self.particles:
                self.done = True

    def draw(self, screen):
        if self.use_sprites:
            if not self.done:
                screen.blit(self.sprites[self.current_frame], self.position)
        else:
            for particle in self.particles:
                particle.draw(screen)
