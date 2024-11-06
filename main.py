import pygame, sys
from handle_movements import Handle
from tic_tac_toe import Battle
from tiles import Tile
from pytmx.util_pygame import load_pygame

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.sprite_group = pygame.sprite.Group()
        self.camera_offset = pygame.Vector2(0, 0)  # Camera offset to adjust view

        # Load the map
        tmx_data = load_pygame('Graphics/map1.tmx')

        # Cycle through all layers and create tiles
        for layer in tmx_data.layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 128, y * 128)
                    surf = pygame.transform.scale(surf, (128, 128))
                    Tile(pos=pos, surf=surf, groups=self.sprite_group)

        self.clock = pygame.time.Clock()
        self.handle = Handle(500, 650)
        self.BOARD = pygame.image.load("Graphics/Board.png")
        self.X_IMG = pygame.image.load("Graphics/X.png")
        self.O_IMG = pygame.image.load("Graphics/O.png")
        self.FONT = pygame.font.Font("Font/Pixeltype.ttf")

    def update_camera(self):
        # Center the camera on the player
        self.camera_offset.x = self.handle.x_axis - self.screen.get_width() // 2
        self.camera_offset.y = self.handle.y_axis - self.screen.get_height() // 2

    def run(self) -> None:
        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        is_running = False
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_b:
                        self.battle = Battle(self.screen, self.BOARD, self.X_IMG, self.O_IMG, self.FONT, "threebythree")  
                    if event.key == pygame.K_v:
                        self.battle = Battle(self.screen, self.BOARD, self.X_IMG, self.O_IMG, self.FONT, "")

            self.screen.fill((0, 0, 0))
            self.update_camera()  # Update camera offset based on player position

            # Draw tiles with camera offset
            for sprite in self.sprite_group:
                offset_pos = sprite.rect.topleft - self.camera_offset
                self.screen.blit(sprite.image, offset_pos)

            self.handle.handle_mov(event)

            # Draw the character at the correct position relative to the camera
            # if 0 <= self.handle.curr_image < len(self.handle.images):
            #     character_pos = (self.handle.x_axis - self.camera_offset.x, 
            #                      self.handle.y_axis - self.camera_offset.y)
            #     self.screen.blit(self.handle.images[self.handle.curr_image], character_pos)

            if 0 <= self.handle.curr_image < len(self.handle.images):
                image_x = self.handle.x_axis + (self.handle.width - self.handle.images[self.handle.curr_image].get_width()) // 2
                image_y = self.handle.y_axis + (self.handle.height - self.handle.images[self.handle.curr_image].get_height()) // 2

                #self.screen.blit(self.handle.images[self.handle.curr_image], 
                                #(self.handle.x_axis, self.handle.y_axis))

                self.screen.blit(self.handle.images[self.handle.curr_image], (image_x, image_y))
                
                character_rect = pygame.Rect(self.handle.x_axis, self.handle.y_axis, 
                                            self.handle.width, self.handle.height)
                # Draw the rectangle (for visualization)
                pygame.draw.rect(self.screen, (255, 0, 0), character_rect, 2)  # Red rectangle with a thickness of 2 pixels
            else:
                print(f"Error: curr_image index {self.handle.curr_image} is out of range. Total images: {len(self.handle.images)}")
                

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()
