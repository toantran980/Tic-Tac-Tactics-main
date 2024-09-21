import pygame, sys
import movements
#import tic_tac_toe

class Game:
    def __init__(self):

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        # Variable that stores whether we are in a battle or not
        self.battle = None

    def run(self):
        # Add code that stops the player from walking when battling
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                

            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(60)

    def load_assets(self):
        BOARD = pygame.imge.load("Graphics/Board.png").convert_alpha()
        FONT = pygame.font.Font("Font/Pixeltype.ttf", 100)

if __name__ == '__main__':
    game = Game()
    game.run()
    