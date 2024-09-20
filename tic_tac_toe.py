import pygame, sys

# will eventuall pass which boss is being faced
# will need to create a function for each boss
# will need a function for each ability

# Work in progress
class Battle:
    def __init__(self, player_abilites, opponent_abilites, bg_surf, fonts):
        self.display_surface = pygame.display.get_surface()
        self.bg_surf = bg_surf
        self.player_abilites = player_abilites
        self.opponent_abilites = opponent_abilites
        self.fonts = fonts
        self.ability_data = {'player': player_abilites, 'opponent': opponent_abilites}

    #def setup(self):

    def update(self, dt):
        #outputs background, currently don't have background
        self.display_surface.blit(self.bg_surf, (0,0))

def tic_tac_game(threat):

    WIDTH, HEIGHT = 1280, 720

    # load font
    FONT = pygame.font.Font()
    # load board
    BOARD = pygame.image.load()
    # load image
    X_IMG = pygame.image.load()
    # load image
    O_IMG = pygame.image.load()

    BG_COLOR = (214, 201, 227)

    board = [[1,2,3], [4,5,6], [7,8,9]]
    graphical_board = 

    def render_board(board, ximg, oimg):
        global graphical_board
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    # Create an x image and rect
                    graphical_board[i][j][0] = ximg
                    graphical_board[i][j][0] = ximg.get_rect(center = (j*300+150, i*300*150))
                elif board[i][j] == 'O':
                    graphical_board[i][j][0] = oimg
                    graphical_board[i][j][0] = oimg.get_rect(center = (j*300+150, i*300*150))

    def add_XO(board, graphical_board, to_move):
        current_pos = pygame.mouse.get_pos()
        converted_x = (current_pos[0]-65)/835*2
        converted_y = current_pos[1]/835*2
        if board[round(converted_y)][round(converted_x)] != 'O' and board[round(converted_y)][round(converted_x)] == 'X':
            board[round(converted_y)][round(converted_x)] = to_move
            if  to_move == 'O':
                to_move = 'X'
            else:
                to_move = 'O'

        render_board(board, X_IMG, O_IMG)

        for i in range(3):
            for j in range(3):
                if graphical_board[i][j][0] is not None:
                    game.screen.blit(graphical_board[i][j][0], graphical_board[i][j][1])
        
        return board, to_move