import pygame
from load_images import Image

class Handle:
    def __init__(self, x, y) -> None:
        self.x_axis = x
        self.y_axis = y 
        self.curr_image = 0
        self.counter = 0
        self.direction = 'idle_up'
        self.vel_y = 0
        self.speed = 3
        self.walk_cooldown = 20
        self.is_moving = False
        
        self.gravity = 0.5  
        self.jump_strength = -15 
        self.on_ground = True  
        self.ground_level = 500

        self.load_images()
        self.images = self.idle_image
        self.rect = pygame.Rect(self.x_axis, self.y_axis, self.width, self.height)
        
        # Check if there are images loaded
        """if self.idle_image:  
            # Use the first image to create the rect
            self.rect = self.idle_image[0].get_rect()  
            self.rect.x = x
            self.rect.y = y
        else:
            self.rect = pygame.Rect(x, y, 0, 0)"""

        
    def load_images(self) -> None:
        try:
            self.load = Image()
            self.down_images = self.load.load_down_images()
            self.up_images = self.load.load_up_images()
            self.left_images = self.load.load_left_images()
            self.right_images = self.load.load_right_images()
            self.idle_image = self.load.load_idle_image(self.direction)

            if self.idle_image:
                self.width = self.idle_image[0].get_width() + 10
                self.height = self.idle_image[0].get_height() + 10

        except pygame.error as errorMessage:
            print(f'Error: {errorMessage}')
    
    def handle_mov(self, event) -> None:
        if event.type == pygame.KEYDOWN:

            directions = {
                pygame.K_UP: ('up', -self.speed),
                pygame.K_DOWN: ('down', self.speed),
                pygame.K_RIGHT: ('right', self.speed),
                pygame.K_LEFT: ('left', -self.speed)
            }
            
            for key, (direction, step) in directions.items():
                if event.key == key:
                    if direction in ['left', 'right']:
                        self.x_axis += step
                        if self.x_axis < 0:
                            self.x_axis = 0
                        elif self.x_axis + self.width > 1280:
                            self.x_axis = 1280 - self.width
                    else:
                        self.y_axis += step 
                        if self.y_axis < 0:
                            self.y_axis = 0
                        elif self.y_axis + self.height > 720:
                            self.y_axis = 720 - self.height

                    self.counter += 1
                    self.direction = direction   
                    self.is_moving = True
                else:
                    self.is_moving = False

            # Handle jumping
            """if event.key == pygame.K_j and self.on_ground:  # Check if space is pressed and on ground
                self.vel_y = -self.jump_strength  # Set upward velocity
                self.on_ground = False  # Set to False when jumping

            if (event.key == pygame.K_j) == False:
                self.on_ground = False
                
            self.y_axis += self.vel_y"""

        if event.type == pygame.KEYUP:
            # Reset the counter when a key is released
            self.counter = 0
            self.is_moving = False
            self.images = self.idle_image
            self.curr_image = 0

        # Update vertical position with gravity
        #self.vel_y += self.gravity  # Apply gravity
        #self.y_axis += self.vel_y  # Update vertical position

        # Check if the character is on the ground
        #self.vel_y += 1
        """if self.y_axis >= self.ground_level:  # Use the defined ground_level
            self.y_axis = self.ground_level  # Reset position to ground level
            self.vel_y = 0  # Reset vertical velocity
            self.on_ground = True  # Set to True when on the ground"""

        # Update rect position
        self.rect.x = self.x_axis
        self.rect.y = self.y_axis 


        # Set the character's animation based on the direction
        if self.direction in ['left', 'right', 'up', 'down']:
            self.images = getattr(self, f'{self.direction}_images')
        else:
            self.images = self.idle_image

        if self.counter >= self.walk_cooldown:  # Adjust the threshold as needed
            # Cycle through images for the leg movement
            if len(self.images) > 0: 
                self.curr_image = (self.curr_image + 1) % len(self.images)
            self.counter = 0

