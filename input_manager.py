import pygame

class PlayerInputHandler:
    def __init__(self):
        self.selected_tower = 0
        self.aim_position = (0, 0)  

    def update(self):
        # Update the aim position based on mouse position
        self.aim_position = pygame.mouse.get_pos()

        # Check for spacebar press to switch towers
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.selected_tower = (self.selected_tower + 1) % 3

    def get_aim_position(self):
        return self.aim_position

    def get_selected_tower(self):
        return self.selected_tower
