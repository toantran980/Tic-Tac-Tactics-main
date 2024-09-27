import pygame, sys
from handle_movements import Handle
from tic_tac_toe import Battle
# from load_images import Image
#import tic_tac_toe

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
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
                        self.battle = Battle(self.screen, self.BOARD, self.X_IMG, self.O_IMG, self.FONT)
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
    