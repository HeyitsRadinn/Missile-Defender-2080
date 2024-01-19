# David Wu

# Importing necessary libraries
import pygame
import random

# Define the Particle class
class Particle:
    def __init__(self, x, y, lifespan):
        # Initialize particle properties: position, size, color, lifespan, and velocity
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
        self.color = (255, random.randint(0, 100), 0)  # Orange-red color
        self.lifespan = lifespan
        self.velocity = [random.uniform(-1, 1), random.uniform(-3, 0)]  # Random velocity

    def update(self):
        # Update particle position, size, and lifespan
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.size = max(self.size - 0.1, 0)  # Decrease size over time
        self.lifespan -= 1  # Decrease lifespan

    def draw(self, screen):
        # Draw the particle on the screen
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

# Define the ExplosionEffect class
class ExplosionEffect:  
    def __init__(self, position, use_sprites=False):
        # Initialize explosion properties
        self.position = position
        self.use_sprites = use_sprites
        self.particles = []
        self.sprites = []
        self.done = False

        if use_sprites:
            self.load_sprites()  # Load sprites if using sprite-based animation
            self.current_frame = 0
        else:
            self.create_particles()  # Create particles if not using sprites

    def load_sprites(self):
        # Load explosion sprites
        self.sprites = [pygame.image.load('explosion1.png'), pygame.image.load('explosion2.png')]  # etc.
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50  # Set frame rate for sprite animation

    def create_particles(self, particle_count=50):
        # Create a specified number of particles
        for _ in range(particle_count):
            self.particles.append(Particle(self.position[0], self.position[1], random.randint(20, 50)))

    def update(self):
        # Update the explosion effect
        if self.use_sprites:
            # Update sprite animation
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.current_frame += 1
                if self.current_frame == len(self.sprites):
                    self.done = True  # Mark as done when all frames are shown
                    return
        else:
            # Update particles
            for particle in self.particles[:]:
                particle.update()
                if particle.lifespan <= 0 or particle.size <= 0:
                    self.particles.remove(particle)  # Remove dead particles
            if not self.particles:
                self.done = True  # Mark as done when all particles are gone

    def draw(self, screen):
        # Draw the explosion effect on the screen
        if self.use_sprites:
            if not self.done:
                screen.blit(self.sprites[self.current_frame], self.position)
        else:
            for particle in self.particles:
                particle.draw(screen)  # Draw each particle
