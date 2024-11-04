import pygame
from load_images import Image

class Handle:
    def __init__(self, x, y) -> None:
        self.x_axis = x
        self.y_axis = y 
        self.curr_image = 0
        self.counter = 0
        self.direction = 'idle_up'
        self.speed = 3
        self.walk_cooldown = 20
        self.is_moving = False
        
        self.load_images()

    def load_images(self):
        try:
            self.load = Image()
            self.down_images = self.load.load_down_images()
            self.up_images = self.load.load_up_images()
            self.left_images = self.load.load_left_images()
            self.right_images = self.load.load_right_images()
            self.idle_images = self.load.rotation_images()
            self.idle_image_dir = self.load.load_idle_image(self.direction)
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
                    else:
                        self.y_axis += step

                    self.counter += 1
                    self.direction = direction   
                    self.is_moving = True
                else:
                    self.is_moving = False
                    
        #if event.type == pygame.KEYUP:
            #if event.key  in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                #self.is_moving = False

        # Set the character's animation based on the direction
        if self.direction in ['left', 'right', 'up', 'down']:
            self.images = getattr(self, f'{self.direction}_images')
        else:
            self.images = self.idle_image_dir    

        if self.counter >= self.walk_cooldown:  # Adjust the threshold as needed
            # Cycle through images for the leg movement
            self.curr_image = (self.curr_image + 1) % len(self.images)
            self.counter = 0

