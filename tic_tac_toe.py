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


# pass a screen to the function
# should eventually also pass each image so we are not being redundant
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
    graphical_board = [[[None, None], [None, None], [None, None]],
                       [[None, None], [None, None], [None, None]]
                       [[None, None], [None, None], [None, None]]]
    
    to_move = 'X'

    SCREEN.fill(BG_COLOR)
    SCREEN.blit(BOARD, (64,64))

    pygame.display.update()

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

    # Adds X or O to board
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
                    SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])
        
        return board, to_move
    

    game_finished = False

    # will eventually need to write code that also handles a 5x5 board
    # work on reducing redundancy from loading images
    def check_win(board):
        winner = None
        for row in range(0,3):
            if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
                winner = board[row][0]
                for i in range(0,3):
                    # add assets to git
                    graphical_board[row][i][0] = pygame.image.load(f"assests/Winning {winner}.png")
                    SCREEN.blit(graphical_board[row][i][0], graphical_board[row][i][1])
                pygame.display.update()
                return winner
        
        for col in range(0,3):
            if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
                winner = board[0][col]
                print(graphical_board[0][col])
                for i in range(0, 3):
                    graphical_board[i][col][0] = pygame.image.load(f"assests/Winning {winner}.png")
                    SCREEN.blit(graphical_board[i][col][0], graphical_board[i][col][1])
                pygame.display.update()
                return winner
            
        if (board[0][0] == board[1][1] == board[2][2] and (board[0][0]) is not None):
            winner = board[0][0]
            graphical_board[0][0][0] = pygame.image.load(f"assets/Winning {winner}.png")
            SCREEN.blit(graphical_board[0][0][0], graphical_board[0][0][1])
            graphical_board[1][1][0] = pygame.image.load(f"assets/Winning {winner}.png")
            SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
            graphical_board[2][2][0] = pygame.image.load(f"assets/Winning {winner}.png")
            SCREEN.blit(graphical_board[2][2][0], graphical_board[2][2][1])
            pygame.display.update()
            return winner
        
        if(board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
            winner = board[0][2]
            graphical_board[0][2][0] = pygame.image.load(f"assets/Winning {winner}.png")
            SCREEN.blit(graphical_board[0][2][0], graphical_board[0][2][1])
            graphical_board[1][1][0] = pygame.image.load(f"assets/Winning {winner}.png")
            SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][0])
            graphical_board[2][0][0] = pygame.image.load(f"assets/Winning {winner}.png")
            SCREEN.blit(graphical_board[2][0][0], graphical_board[2][0][1])
            pygame.display.update()
            return winner
        
        if winner is None:
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] != 'X' and board[i][j] != 'O':
                        return None
            return "DRAW"


    # Still want player to be capable of closing the screen while in combat
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                board, to_move = add_XO(board, graphical_board, to_move)

                if game_finished:
                    board = [[1,2,3], [4,5,6], [7,8,9]]
                    graphical_board = [[[None, None], [None, None], [None, None]],
                                    [[None, None], [None, None], [None, None]]
                                    [[None, None], [None, None], [None, None]]]
    
                    to_move = 'X'
                    game_finsihed = False
   
                    SCREEN.fill(BG_COLOR)
                    SCREEN.blit(BOARD, (64,64))

                    pygame.display.update()

                    if check_win(board) is not None:
                        game_finished = True

                    pygame.display.update()