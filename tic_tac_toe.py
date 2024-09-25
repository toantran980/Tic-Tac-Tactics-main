import pygame, sys

# will eventuall pass which boss is being faced
# will need to create a function for each boss
# will need a function for each ability

# Work in progress
# def __init__(self, player_abilites, opponent_abilites, bg_surf, fonts):
    #     self.display_surface = pygame.display.get_surface()
    #     self.bg_surf = bg_surf
    #     self.player_abilites = player_abilites
    #     self.opponent_abilites = opponent_abilites
    #     self.fonts = fonts
    #     self.ability_data = {'player': player_abilites, 'opponent': opponent_abilites}

    # #def setup(self):

    # def update(self, dt):
    #     #outputs background, currently don't have background
    #     self.display_surface.blit(self.bg_surf, (0,0))
class Battle:

    # pass a screen to the function
    # should eventually also pass each image so we are not being redundant
    def __init__(self, SCREEN, BOARD, X_IMG, O_IMG, FONT):
        # load font
        # FONT = pygame.font.Font()
        # load board
        # BOARD = pygame.image.load()
        # load image
        # X_IMG = pygame.image.load()
        # load image
        # O_IMG = pygame.image.load()

        self.SCREEN = SCREEN
        self.BOARD = BOARD
        self.X_IMG = X_IMG
        self.O_IMG = O_IMG
        self.FONT = FONT
        self.BG_COLOR = (214, 201, 227)

        self.board = [[1,2,3], [4,5,6], [7,8,9]]
        self.graphical_board = [[[None, None], [None, None], [None, None]],
                        [[None, None], [None, None], [None, None]],
                        [[None, None], [None, None], [None, None]]]
        
        self.to_move = 'X'

        SCREEN.fill(self.BG_COLOR)
        SCREEN.blit(BOARD, (64,64))

        pygame.display.update()
        # Still want player to be capable of closing the screen while in combat
        game_finished = False
        con = True
        escape = True
        while escape:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and con:
                    self.board, self.to_move = self.add_XO(self.board, self.graphical_board, self.to_move)

                    if game_finished:
                        self.board = [[1,2,3], [4,5,6], [7,8,9]]
                        self.graphical_board = [[[None, None], [None, None], [None, None]],
                                        [[None, None], [None, None], [None, None]],
                                        [[None, None], [None, None], [None, None]]]
        
                        self.to_move = 'X'
                        game_finished = False
    
                        self.SCREEN.fill(self.BG_COLOR)
                        self.SCREEN.blit(self.BOARD, (64,64))

                        pygame.display.update()

                    result = self.check_win(self.board)
                    if result is not None:
                        game_finished = True
                        if result == "DRAW":
                            # Handle draw case
                            print("Game ended in a draw")
                            con = True  # Stop taking moves
                        else:
                            # Handle win case
                            print(f"{result} wins!")
                            con = False  # Stop taking moves


                    pygame.display.update()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    escape = False


    def render_board(self, board, ximg, oimg):
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    # Create an X image and rect
                    self.graphical_board[i][j][0] = ximg
                    self.graphical_board[i][j][1] = ximg.get_rect(center=(j*300+150, i*300+150))
                elif board[i][j] == 'O':
                    # Create an O image and rect
                    self.graphical_board[i][j][0] = oimg
                    self.graphical_board[i][j][1] = oimg.get_rect(center=(j*300+150, i*300+150))

    # Adds X or O to board
    def add_XO(self, board, graphical_board, to_move):
        current_pos = pygame.mouse.get_pos()
        # Adjust these based on your board's position and size
        converted_x = (current_pos[0] - 64) // (835 // 3)  # Assume board starts at x=64 and size 835px
        converted_y = (current_pos[1] - 64) // (835 // 3)  # Same for y position

        # Ensure converted_x and converted_y are valid indices
        if 0 <= converted_x < 3 and 0 <= converted_y < 3:
            # Check if the cell is empty (i.e., not 'X' or 'O')
            if board[int(converted_y)][int(converted_x)] not in ['X', 'O']:
                # Place the current move (either 'X' or 'O')
                board[int(converted_y)][int(converted_x)] = to_move
                # Switch turns
                to_move = 'O' if to_move == 'X' else 'X'

        # Render the board after making the move
        self.render_board(board, self.X_IMG, self.O_IMG)

        # Display updated images for X and O
        for i in range(3):
            for j in range(3):
                if graphical_board[i][j][0] is not None:
                    self.SCREEN.blit(self.graphical_board[i][j][0], self.graphical_board[i][j][1])
                
        return board, to_move

    # will eventually need to write code that also handles a 5x5 board
    # work on reducing redundancy from loading images
    def check_win(self, board):
        winner = None
        for row in range(0,3):
            if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
                winner = board[row][0]
                for i in range(0,3):
                    # add assets to git
                    self.graphical_board[row][i][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
                    self.SCREEN.blit(self.graphical_board[row][i][0], self.graphical_board[row][i][1])
                pygame.display.update()
                return winner
            
        for col in range(0,3):
            if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
                winner = board[0][col]
                print(self.graphical_board[0][col])
                for i in range(0, 3):
                    self.graphical_board[i][col][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
                    self.SCREEN.blit(self.graphical_board[i][col][0], self.graphical_board[i][col][1])
                pygame.display.update()
                return winner
                
        if (board[0][0] == board[1][1] == board[2][2] and (board[0][0]) is not None):
            winner = board[0][0]
            self.graphical_board[0][0][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[0][0][0], self.graphical_board[0][0][1])
            self.graphical_board[1][1][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[1][1][0], self.graphical_board[1][1][1])
            self.graphical_board[2][2][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[2][2][0], self.graphical_board[2][2][1])
            pygame.display.update()
            return winner
            
        if(board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
            winner = board[0][2]
            self.graphical_board[0][2][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[0][2][0], self.graphical_board[0][2][1])
            self.graphical_board[1][1][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[1][1][0], self.graphical_board[1][1][1])
            self.graphical_board[2][0][0] = pygame.image.load(f"Graphics/Winning {winner}.png")
            self.SCREEN.blit(self.graphical_board[2][0][0], self.graphical_board[2][0][1])
            pygame.display.update()
            return winner
            
        if winner is None:
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] != 'X' and board[i][j] != 'O':
                        return None
            return "DRAW"