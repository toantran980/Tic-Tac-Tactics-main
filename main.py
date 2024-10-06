import pygame, sys
from handle_movements import Handle
from tic_tac_toe import Battle
from pytmx.util_pygame import load_pygame
# from load_images import Image
#import tic_tac_toe

# class Tile(pygame.sprite.Sprite):
#     def __init__(self, pos, surf, groups):
#         super().__init__(groups)
#         self.image - surf
#         self.rect = self.image.get_rect(topleft = pos)

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        #map
        tmx_data = load_pygame('Graphics/map1.tmx')
        # sprite_group = pygame.sprite.Group()

        # #cycle through all layers
        # for layer in tmx_data.layers:
        #     if hasattr(layer, 'data'):
        #         for x,y,surf in layer.tiles():
        #             pos = (x * 128, y * 128)
        #             Tile(pos = pos, surf = surf, groups = sprite_group)


        self.clock = pygame.time.Clock()
        self.handle = Handle(500, 650)
        self.map = pygame.image.load('Graphics/map1.png')
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
                        self.battle = Battle(self.screen, self.BOARD, self.X_IMG, self.O_IMG, self.FONT, "threebythree")
                        # self.screen.fill("black")
                        # pygame.display.flip()


            self.screen.blit(self.map, (0, 0))
            self.handle.handle_mov(event)
            self.screen.blit(self.handle.images[self.handle.curr_image], 
                            (self.handle.x_axis, self.handle.y_axis))

            pygame.display.flip()
            self.clock.tick(60)
    

    # def load_assets(self):
    #     BOARD = pygame.imge.load("Graphics/Board.png").convert_alpha()
    #     FONT = pygame.font.Font("Font/Pixeltype.ttf", 100)

if __name__ == '__main__':
    game = Game()
    game.run()
    