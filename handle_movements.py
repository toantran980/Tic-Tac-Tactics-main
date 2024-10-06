import pygame
from load_images import Image

SPEED = 1

class Handle:
    def __init__(self, x, y) -> None:
        self.x_axis = x
        self.y_axis = y 
        self.curr_image = 0
        self.image_counter = 0
        self.direction = 'right' 
        # self.direction = 'idle'---> need to set idle state as DEFAULT STATE, no legs move

        try:
            self.load = Image()
            self.down_images = self.load.load_down_images()
            self.up_images = self.load.load_up_images()
            self.left_images = self.load.load_left_images()
            self.right_images = self.load.load_right_images()
            # self.idle_images = self.load.load_idle_images()
        except pygame.error as errorMessage:
            print(f'Error: {errorMessage}')
    
    def handle_mov(self, event) -> None:
        
        # self.images = self.idle_images
        if event.type == pygame.KEYDOWN:
            directions = {
                pygame.K_UP: ('up', -SPEED),
                pygame.K_DOWN: ('down', SPEED),
                pygame.K_RIGHT: ('right', SPEED),
                pygame.K_LEFT: ('left', -SPEED)
            }
            
            for key, (direction, step) in directions.items():
                if event.key == key:
                    if direction in ['left', 'right']:
                        self.x_axis += step
                    else:
                        self.y_axis += step

                    self.direction = direction
                    self.curr_image = 0
                
        # Set the character's animation to directions
        if self.direction in ['left', 'right', 'up', 'down']:
            self.images = getattr(self, f'{self.direction}_images')
    
        self.image_counter += 1
        if self.image_counter >= 10:
            # images rotation mechanisms
            self.curr_image = (self.curr_image + 1) % len(self.images)
            self.image_counter = 0