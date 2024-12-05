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
                        # Constrain to map width
                        self.x_axis = max(0, min(self.x_axis, 1280 * 10 - self.width))  # Example for a large map
                    else:
                        self.y_axis += step
                        # Constrain to map height
                        self.y_axis = max(0, min(self.y_axis, 720 * 10 - self.height))  # Example for a large map

                    self.counter += 1
                    self.direction = direction
                    self.is_moving = True
                else:
                    self.is_moving = False

        if event.type == pygame.KEYUP:
            self.counter = 0
            self.is_moving = False
            self.images = self.idle_image
            self.curr_image = 0

        # Update rect position
        self.rect.x = self.x_axis
        self.rect.y = self.y_axis

        # Set the character's animation based on the direction
        if self.direction in ['left', 'right', 'up', 'down']:
            self.images = getattr(self, f'{self.direction}_images')
        else:
            self.images = self.idle_image

        if self.counter >= self.walk_cooldown:  # Adjust the threshold as needed
            if len(self.images) > 0:
                self.curr_image = (self.curr_image + 1) % len(self.images)
            self.counter = 0


