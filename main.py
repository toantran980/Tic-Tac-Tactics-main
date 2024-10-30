import pygame, sys
from handle_movements import Handle
from tic_tac_toe import Battle
from tiles import Tile
from pytmx.util_pygame import load_pygame
from tiles import Tile
# from load_images import Image

<<<<<<< HEAD


=======
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
    
>>>>>>> 14024b0ae7f7671b0acff1d30b03bb1bbdc12edd
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))

        self.sprite_group = pygame.sprite.Group()

        # Load the map
        tmx_data = load_pygame('Graphics/map1.tmx')

        # Cycle through all layers and create tiles
        for layer in tmx_data.layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 128, y * 128)
                    surf = pygame.transform.scale(surf, (128,128))
                    Tile(pos=pos, surf=surf, groups=self.sprite_group)

        self.clock = pygame.time.Clock()
        self.handle = Handle(500, 650)
        self.BOARD = pygame.image.load("Graphics/Board.png")
        self.X_IMG = pygame.image.load("Graphics/X.png")
        self.O_IMG = pygame.image.load("Graphics/O.png")
        self.FONT = pygame.font.Font("Font/Pixeltype.ttf")

        # Variable that stores whether we are in a battle or not

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
<<<<<<< HEAD
                        self.battle = Battle(self.screen, self.BOARD, self.X_IMG, self.O_IMG, self.FONT, "threebythree")  
=======
                        self.battle = Battle(self.screen, self.BOARD, self.X_IMG, self.O_IMG, self.FONT, "threebythree")
>>>>>>> 928be1db18debc1663e39167a1a59cf45a1684da
                    if event.key == pygame.K_v:
                        self.battle = Battle(self.screen, self.BOARD, self.X_IMG, self.O_IMG, self.FONT, "")

                #self.handle.handle_mov(event)
            # Clear the screen (optional, if you want to have a clean canvas every frame)
            self.screen.fill((0, 0, 0))  

            # Draw the map tiles (using self.sprite_group)
            self.sprite_group.draw(self.screen)

            self.handle.handle_mov(event)
    
            if 0 <= self.handle.curr_image < len(self.handle.images):
                self.screen.blit(self.handle.images[self.handle.curr_image], 
                                (self.handle.x_axis, self.handle.y_axis))
            else:
                print(f"Error: curr_image index {self.handle.curr_image} is out of range. Total images: {len(self.handle.images)}")
                

            pygame.display.flip()
            self.clock.tick(60)

    #def load_assets(self):
        #BOARD = pygame.imge.load("Graphics/Board.png").convert_alpha()
        #FONT = pygame.font.Font("Font/Pixeltype.ttf", 100)


if __name__ == '__main__':
    game = Game()
    game.run()
