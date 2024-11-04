import pygame

class Image:
    def __init__(self):
        self.down_images = []
        self.up_images = []
        self.left_images = []
        self.right_images = []
        # self.idle_images = []

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
    

    """def load_idle_images(self)->list:
        for i in range(1, 1):
            image = pygame.image.load(f'Character_Sprite/back_{i}.png')
            self.up_images.append(image)
        return self.up_images"""