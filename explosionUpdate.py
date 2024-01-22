# David Wu
# Explosion part

# Import the pygame module for game development and the random module for generating random numbers
import pygame
import random

# Define a Particle class to represent each individual particle in the explosion
class Particle:
    def __init__(self, x, y, lifespan):
        # Initialize the particle's position, size, color, lifespan, and velocity
        self.x = x  # X-coordinate
        self.y = y  # Y-coordinate
        self.size = random.randint(2, 5)  # Random size between 2 and 5
        self.color = (255, random.randint(0, 100), 0)  # Orange-red color with random green component
        self.lifespan = lifespan  # Lifespan of the particle
        # Random velocity components for movement
        self.velocity = [random.uniform(-1, 1), random.uniform(-3, 0)]

    def update(self):
        # Update the particle's position, size, and lifespan
        self.x += self.velocity[0]  # Update x-coordinate
        self.y += self.velocity[1]  # Update y-coordinate
        self.size = max(self.size - 0.1, 0)  # Decrease size over time
        self.lifespan -= 1  # Decrease lifespan

    def draw(self, screen):
        # Draw the particle on the screen
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

# Define an ExplosionEffect class to manage the explosion effect
class ExplosionEffect:
    def __init__(self, position, use_sprites=False):
        # Initialize the explosion effect with position, sprite usage, particles, sprites, and completion status
        self.position = position  # Position of the explosion
        self.use_sprites = use_sprites  # Boolean to decide between particle effect and sprite animation
        self.particles = []  # List of particles
        self.sprites = []  # List of sprites for the explosion
        self.done = False  # Flag to indicate if the effect is completed

        if use_sprites:
            self.load_sprites()  # Load sprites if use_sprites is True
            self.current_frame = 0
        else:
            self.create_particles()  # Create particles if use_sprites is False

    def load_sprites(self):
        # Load explosion sprites and set up sprite animation parameters
        # Replace with actual sprite file names
        self.sprites = [pygame.image.load('explosion1.png'), pygame.image.load('explosion2.png')]  # etc.
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50  # Frame rate for sprite animation

    def create_particles(self, particle_count=50):
        # Create particles for the explosion effect
        for _ in range(particle_count):
            self.particles.append(Particle(self.position[0], self.position[1], random.randint(20, 50)))

    def update(self):
        # Update the explosion effect based on whether sprites or particles are used
        if self.use_sprites:
            # Update sprite animation
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.current_frame += 1
                if self.current_frame == len(self.sprites):
                    self.done = True  # End the effect if all frames have been shown
        else:
            # Update particle effect
            for particle in self.particles[:]:
                particle.update()
                if particle.lifespan <= 0 or particle.size <= 0:
                    self.particles.remove(particle)
            if not self.particles:
                self.done = True  # End the effect if all particles are gone

    def draw(self, screen):
        # Draw the explosion effect on the screen
        if self.use_sprites:
            # Draw sprite animation
            if not self.done:
                screen.blit(self.sprites[self.current_frame], self.position)
        else:
            # Draw particles
            for particle in self.particles:
                particle.draw(screen)
