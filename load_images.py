import pygame

class Image:
    def __init__(self):
        self.down_images = []
        self.up_images = []
        self.left_images = []
        self.right_images = []
        self.idle_images = []
        self.idle_up_image = []
        self.idle_down_image = []
        self.idle_left_image = []
        self.idle_right_image = []

    def load_down_images(self) -> list:
        for i in range(1, 5):  
            image = pygame.image.load(f'Character_Sprite/forward_{i}.png')
            self.down_images.append(image)
        return self.down_images

    def load_up_images(self)-> list:
        for i in range(1, 5):  
            image = pygame.image.load(f'Character_Sprite/back_{i}.png')
            self.up_images.append(image)
        return self.up_images

    def load_left_images(self)-> list:
        for i in range(1, 5): 
            image = pygame.image.load(f'Character_Sprite/left_{i}.png')
            self.left_images.append(image)
        return self.left_images

    def load_right_images(self)-> list:
        for i in range(1, 5):  
            image = pygame.image.load(f'Character_Sprite/right_{i}.png')
            self.right_images.append(image)
        return self.right_images
    
    def rotation_images(self)-> list:
        for i in range(1, 5):  
            image = pygame.image.load(f'Character_Sprite/idle_{i}.png')
            self.idle_images.append(image)
        return self.idle_images
    
    
    def load_idle_image(self, direction: str) -> list:
        # Dictionary to map directions to their corresponding image file names
        image_files = {
            'idle_up': 'Character_Sprite/idle_1.png',
            'idle_down': 'Character_Sprite/idle_2.png',
            'idle_left': 'Character_Sprite/idle_3.png',
            'idle_right': 'Character_Sprite/idle_4.png'
        }

        # Check if the provided direction is valid
        if direction in image_files:
            # Load the image
            image = pygame.image.load(image_files[direction])
            
            # Append the image to the corresponding list based on the direction
            if direction == 'idle_up':
                self.idle_up_image.append(image)
                return self.idle_up_image
            elif direction == 'idle_down':
                self.idle_down_image.append(image)
                return self.idle_down_image
            elif direction == 'idle_left':
                self.idle_left_image.append(image)
                return self.idle_left_image
            elif direction == 'idle_right':
                self.idle_right_image.append(image)
                return self.idle_right_image
        else:
            raise ValueError("Invalid direction. Please use 'up', 'down', 'left', or 'right'.")