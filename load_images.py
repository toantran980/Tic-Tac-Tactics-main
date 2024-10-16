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
    
    def load_idle_up_image(self)->list:
        # for i in range(1, 5):
        image = pygame.image.load('Character_Sprite/idle_1.png')
        self.idle_up_image.append(image)
        return self.idle_up_image
    
    def load_idle_down_image(self)->list:
        # for i in range(1, 5):
        image = pygame.image.load('Character_Sprite/idle_2.png')
        self.idle_down_image.append(image)
        return self.idle_down_image

    def load_idle_left_image(self)->list:
        # for i in range(1, 5):
        image = pygame.image.load('Character_Sprite/idle_3.png')
        self.idle_left_image.append(image)
        return self.idle_left_image

    def load_idle_right_image(self)->list:
        # for i in range(1, 5):
        image = pygame.image.load('Character_Sprite/idle_4.png')
        self.idle_right_image.append(image)
        return self.idle_right_image