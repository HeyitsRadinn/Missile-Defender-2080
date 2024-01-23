import pygame, math

screen = pygame.display.set_mode((850, 750), 0, 32)
fps = pygame.time.Clock()

imgBGImage = 'BG.jpg'
imgTarget = 'assets/crosshair.png'
imgcannon = 'assets/cannon.png'


BG = pygame.image.load(imgBGImage).convert()
cannonL = pygame.transform.scale(pygame.image.load(imgcannon), (350, 50)).convert_alpha()
cannonM = pygame.transform.scale(pygame.image.load(imgcannon), (350, 50)).convert_alpha()
cannonR = pygame.transform.scale(pygame.image.load(imgcannon), (350, 50)).convert_alpha()
Target = pygame.transform.scale((pygame.image.load(imgTarget)), (30, 30)).convert_alpha()


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


class PlayerInputHandler:
    def __init__(self):
        self.selected_tower = 0
        self.active = 0
        self.aim_position = (0, 0)
        self.tower_positions = [(200,700), (400,700), (600,700)] # need to determine coords for towers 
        self.missilecount = 10
        self.missiles = []
        self.image = [0, 1, 2]
        self.image[0] = pygame.transform.scale(pygame.image.load(imgcannon), (350, 50)).convert_alpha()
        self.image[1] = pygame.transform.scale(pygame.image.load(imgcannon), (350, 50)).convert_alpha()
        self.image[2] = pygame.transform.scale(pygame.image.load(imgcannon), (350, 50)).convert_alpha()


    def switchcannon(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    self.selected_tower = (self.selected_tower + 1) % 3

    def draw(self):
        for i in range(len(self.tower_positions)):
            cannon_image = self.image[i]
            tower_position = self.tower_positions[i]
            screen.blit(cannon_image, tower_position)
    
    def shoot(self):
        self.aim_position = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if self.missilecount == 0:
                pass
            else:
                self.missiles = Missile(self.tower_positions[self.selected_tower], self.aim_position, 5)
                
                self.missiles.draw(screen)
                self.missiles.MoveTowardsDestination()
                self.missiles.draw(screen)
                self.missilecount -= 1

        
def rotatepic(image, angle):
    rotated_images = []
    
    for img in image:
        orig_rect = img.get_rect()
        
        # Set the rotation center to the bottom center of the image
        rotation_center = orig_rect.midbottom
        
        rotated_image = pygame.transform.rotate(img, angle)
    
        new_rect = rotated_image.get_rect(center=rotation_center)
        rotated_surface = pygame.Surface((max(new_rect.width, orig_rect.width), max(new_rect.height, orig_rect.height)), pygame.SRCALPHA)
    
        rotated_surface.blit(rotated_image, (rotated_surface.get_width() // 2 - new_rect.width // 2, 
                                            rotated_surface.get_height() - new_rect.height))
    
        rotated_images.append(rotated_surface)
    
    return rotated_images



def AngleDifference(X1, Y1, X2, Y2):
    return math.degrees(math.atan2(Y1 - Y2, X2 - X1))


person = PlayerInputHandler()

x1, y1 = person.tower_positions[person.selected_tower]

RunGame = True

while RunGame:
    fps.tick(32)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunGame = False

    TargetX, TargetY = pygame.mouse.get_pos()
    Angle = AngleDifference(x1, y1, TargetX, TargetY)

    # Set the rotation center to a specific point relative to the center of the cannon image
    rotation_center_offset = (20, -50)  # Adjust the offset as needed
    Rotatedcannon = rotatepic(person.image, Angle)


    for rotated_surface in Rotatedcannon:
        BlitOffsetX = rotated_surface.get_width() / 2
        BlitOffsetY = rotated_surface.get_height() / 2

    person.draw()

    screen.blit(BG, (0, 0))

    for rotated_surface in Rotatedcannon:
        screen.blit(rotated_surface, (x1 - BlitOffsetX, y1 - BlitOffsetY))
    screen.blit(Target, (TargetX - 15, TargetY - 15))
    person.shoot()
    pygame.display.update()
