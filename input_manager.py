# David Wu

# Importing the pygame library
import pygame

# Define the PlayerInputHandler class
class PlayerInputHandler:
    def __init__(self):
<<<<<<< HEAD
        # Initialize selected tower and aim position
        self.selected_tower = 0  # Default selected tower index
        self.aim_position = (0, 0)  # Default aim position
=======
        self.selected_tower = 0
        self.aim_position = (0, 0)  
>>>>>>> d9b6d6f4a256c7f41618f14df8aee7d6befb4152

    def update(self):
        # Update the player's input state
        # Update the aim position based on the current mouse position
        self.aim_position = pygame.mouse.get_pos()

        # Process events from the event queue
        for event in pygame.event.get():
            # Check if a key is pressed
            if event.type == pygame.KEYDOWN:
                # Switch to the next tower if the spacebar is pressed
                if event.key == pygame.K_SPACE:
                    # Cycle through towers (0, 1, 2) when spacebar is pressed
                    self.selected_tower = (self.selected_tower + 1) % 3

    def get_aim_position(self):
        # Return the current aim position
        return self.aim_position

    def get_selected_tower(self):
        # Return the currently selected tower index
        return self.selected_tower
