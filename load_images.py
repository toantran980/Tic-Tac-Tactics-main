import pygame

class Image:
    def __init__(self):
        self.down_images = []
        self.up_images = []
        self.left_images = []
        self.right_images = []
    
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

    def load_idle_image(self, direction: str) -> list:
        # Dictionary to map directions to their corresponding image file names
        image_files = {
        'idle_up': 'Character_Sprite/idle_1.png',
        'idle_down': 'Character_Sprite/idle_2.png',
        'idle_left': 'Character_Sprite/idle_3.png',
        'idle_right': 'Character_Sprite/idle_4.png'
    }

        if direction in image_files:
            image = pygame.image.load(image_files[direction])

            curr_attribute = f'idle_{direction.split("_")[1]}_image'
            
            # Use getattr to append the image to the corresponding idle image list
            current_idle_images = getattr(self, curr_attribute, [])
            current_idle_images.append(image)
            # Update the attribute with the new list
            setattr(self, curr_attribute, current_idle_images)
            return current_idle_images

        else:
            raise ValueError("Invalid direction provided.")
