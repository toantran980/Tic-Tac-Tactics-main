import pygame, sys
import random

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
    def __init__(self, SCREEN, BOARD, X_IMG, O_IMG, FONT, gametype):

        self.SCREEN = SCREEN
        self.BOARD = BOARD
        self.X_IMG = X_IMG
        self.O_IMG = O_IMG
        self.FONT = FONT
        self.BG_COLOR = (214, 201, 227)

        if gametype == "threebythree":
            self.threebythree()
        else:
            self.fivebyfive()

    # need to implement function that clears the board
    def fivebyfive(self):
        self.board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 
                    [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], 
                    [21, 22, 23, 24, 25]]
        self.graphical_board = [[[None, None] for _ in range(5)] for _ in range(5)]
        self.ai_move_count = 0
        self.to_move = 'X'
        square_size = 772 // 5  # Each square is 154 pixels wide for a 5x5 board
        x_offset = 64  # Offset from the left edge of the screen

        # Fill background and draw the board grid
        self.SCREEN.fill(self.BG_COLOR)

        for i in range(1, 5):  # Draw grid lines (4 lines horizontally and vertically)
            pygame.draw.line(self.SCREEN, (0, 0, 50), (x_offset, i * square_size), (772 + x_offset, i * square_size), 10)
            pygame.draw.line(self.SCREEN, (0, 0, 50), (i * square_size + x_offset, 0), (i * square_size + x_offset, 772), 10)

        pygame.display.update()

        # Resizing the X and O images to fit inside each square
        self.X_IMG = pygame.transform.scale(self.X_IMG, (square_size - 10, square_size - 10))
        self.O_IMG = pygame.transform.scale(self.O_IMG, (square_size - 10, square_size - 10))

        game_finished = False
        con = True
        escape = True

        while escape:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and con:
                    self.board, self.to_move = self.add_XO_fivebyfive(self.board, self.graphical_board, self.to_move)
                    
                    if game_finished:
                        self.board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 
                                      [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], 
                                      [21, 22, 23, 24, 25]]
                        self.graphical_board = [[[None, None] for _ in range(5)] for _ in range(5)]

                        self.to_move = 'X'
                        square_size = 772 // 5  # Each square is 154 pixels wide for a 5x5 board
                        x_offset = 64  # Offset from the left edge of the screen
                        self.ai_move_count = 0
                        # Fill background and draw the board grid
                        self.SCREEN.fill(self.BG_COLOR)

                        for i in range(1, 5):  # Draw grid lines (4 lines horizontally and vertically)
                            pygame.draw.line(self.SCREEN, (0, 0, 50), (x_offset, i * square_size), (772 + x_offset, i * square_size), 10)
                            pygame.draw.line(self.SCREEN, (0, 0, 50), (i * square_size + x_offset, 0), (i * square_size + x_offset, 772), 10)

                        pygame.display.update()

                    result = self.check_win_fivebyfive(self.board)
                    if result is not None:
                        game_finished = True
                        if result == "DRAW":
                            print("Game ended in a draw")
                            con = True  # Stop taking moves
                        else:
                            print(f"{result} wins!")
                            con = False
                        pygame.display.update()  # Update the display after checking for win/draw
                        continue
                    
                    # AI's move (if the game is not finished)
                    if not game_finished and self.to_move == 'O':
                        self.board, self.to_move = self.ai_move_fivebyfive(self.board, self.graphical_board, self.to_move)
                        
                        result = self.check_win_fivebyfive(self.board)
                        if result is not None:
                            game_finished = True
                            if result == "DRAW":
                                print("Game ended in a draw")
                                con = True
                            else:
                                print(f"{result} wins!")
                                con = False
                        pygame.display.update()  # Update the display after AI's move
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    escape = False

    
    # function for 3x3 battles
    def threebythree(self):
        self.board = [[1,2,3], [4,5,6], [7,8,9]]
        self.graphical_board = [[[None, None], [None, None], [None, None]],
                        [[None, None], [None, None], [None, None]],
                        [[None, None], [None, None], [None, None]]]
        
        self.to_move = 'X'

        self.SCREEN.fill(self.BG_COLOR)
        #self.SCREEN.blit(self.BOARD, (-66,-26))

        square_size = 772 // 3  # Each square is about 257 pixels
        x_offset = 100  # Move the grid 100 pixels to the right (adjust as needed)
        for i in range(1, 3):
            # Horizontal lines
            pygame.draw.line(self.SCREEN, (0, 0, 50), (x_offset, i * square_size), (772 + x_offset, i * square_size), 15)
            # Vertical lines
            pygame.draw.line(self.SCREEN, (0, 0, 50), (i * square_size + x_offset, 0), (i * square_size + x_offset, 772), 15)

        

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
                        for i in range(1, 3):
                            # Horizontal lines
                            pygame.draw.line(self.SCREEN, (0, 0, 50), (x_offset, i * square_size), (772 + x_offset, i * square_size), 15)
                            # Vertical lines
                            pygame.draw.line(self.SCREEN, (0, 0, 50), (i * square_size + x_offset, 0), (i * square_size + x_offset, 772), 15)


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
                        continue

                    #pygame.display.update()
                    # AI's turn (if the game is not finish)
                    if not game_finished and self.to_move == 'O':
                        self.board, self.to_move = self.rand_ai_move(self.board, self.graphical_board, self.to_move)

                        result = self.check_win(self.board)
                        if result is not None:
                            game_finished = True
                            if result == "Draw":
                                print("Game ended in a draw")
                                con = True
                            else:
                                print(f"{result} wins!")
                                con = False
                        pygame.display.update()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    escape = False


    def render_board(self, board, ximg, oimg):
        square_size = 772 // 3  # Each square is about 257 pixels
        x_offset = 100  # Move the grid 100 pixels to the right (adjust as needed)

        for i in range(3):
            for j in range(3):
                # Calculate the center of the current square (i, j)
                center_x = j * square_size + square_size // 2 + x_offset
                center_y = i * square_size + square_size // 2

                if board[i][j] == 'X':
                    self.graphical_board[i][j][0] = ximg
                    # Center the X image using get_rect with the calculated center
                    self.graphical_board[i][j][1] = ximg.get_rect(center=(center_x, center_y))
                elif board[i][j] == 'O':
                    self.graphical_board[i][j][0] = oimg
                    # Center the O image using get_rect with the calculated center
                    self.graphical_board[i][j][1] = oimg.get_rect(center=(center_x, center_y))

        # Draw the grid lines with the same offset
        for i in range(1, 3):
            # Horizontal lines
            pygame.draw.line(self.SCREEN, (0, 0, 50), (x_offset, i * square_size), (772 + x_offset, i * square_size), 15)
            # Vertical lines
            pygame.draw.line(self.SCREEN, (0, 0, 50), (i * square_size + x_offset, 0), (i * square_size + x_offset, 772), 15)

    # Adds X or O to board
    def add_XO(self, board, graphical_board, to_move):
        current_pos = pygame.mouse.get_pos()
        
        # Subtract the x_offset (100) before calculating the converted_x position
        converted_x = (current_pos[0] - 100) // (772 // 3)  # Assume board starts at x=100 and size 772px
        converted_y = current_pos[1] // (772 // 3)  # No x_offset for y; y starts from 0

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
        
        return None
    
    # rand_ai_move chooses rand spot on board, will only use for first boss
    def rand_ai_move(self, board, graphical_board, to_move):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] not in ['X', 'O']]

        if empty_cells:
            move = random.choice(empty_cells)
            board[move[0]][move[1]] = 'O'
            to_move = 'X'

        self.render_board(board, self.X_IMG, self.O_IMG)

        for i in range(3):
            for j in range(3):
                if graphical_board[i][j][0] is not None:
                    self.SCREEN.blit(self.graphical_board[i][j][0], self.graphical_board[i][j][1])

        return board, to_move
    
    def render_fivebyfive(self, board, ximg, oimg):
        square_size = 772 // 5  # Each square is 154 pixels for the 5x5 board
        x_offset = 64  # Offset to center the board horizontally
        y_offset = 0   # You can add a vertical offset if needed

        for i in range(5):
            for j in range(5):
                center_x = j * square_size + square_size // 2 + x_offset
                center_y = i * square_size + square_size // 2 + y_offset

                # Check the board and render the appropriate image
                if board[i][j] == 'X':
                    self.graphical_board[i][j][0] = ximg
                    self.graphical_board[i][j][1] = ximg.get_rect(center=(center_x, center_y))
                elif board[i][j] == 'O':
                    self.graphical_board[i][j][0] = oimg
                    self.graphical_board[i][j][1] = oimg.get_rect(center=(center_x, center_y))

        # After assigning the positions, draw all images onto the screen
        for i in range(5):
            for j in range(5):
                if self.graphical_board[i][j][0] is not None:
                    self.SCREEN.blit(self.graphical_board[i][j][0], self.graphical_board[i][j][1])

        # Update the screen after rendering
        pygame.display.update()


    def add_XO_fivebyfive(self, board, graphical_board, to_move):
        current_pos = pygame.mouse.get_pos()

        # Subtract the x_offset (64) and calculate positions based on 5x5 grid
        converted_x = (current_pos[0] - 64) // (772 // 5)
        converted_y = current_pos[1] // (772 // 5)

        # Ensure converted_x and converted_y are valid indices
        if 0 <= converted_x < 5 and 0 <= converted_y < 5:
            # Check if the cell is empty (i.e., not 'X' or 'O')
            if board[int(converted_y)][int(converted_x)] not in ['X', 'O']:
                # Place the current move (either 'X' or 'O')
                board[int(converted_y)][int(converted_x)] = to_move
                # Switch turns
                to_move = 'O' if to_move == 'X' else 'X'

        # Render the board after making the move
        self.render_fivebyfive(board, self.X_IMG, self.O_IMG)

        return board, to_move

    def ai_move_fivebyfive(self, board, graphical_board, to_move):
        self.ai_move_count += 1  # Increment the AI move count

        # For the first three moves, pick a random available move
        if self.ai_move_count <= 3:
            available_moves = [
                (i, j) for i in range(5) for j in range(5) if board[i][j] not in ['X', 'O']
            ]
            if available_moves:
                i, j = random.choice(available_moves)
                board[i][j] = 'O'
        else:
            best_move = None
            best_score = -float('inf')

            # Evaluate all available moves
            for i in range(5):
                for j in range(5):
                    if board[i][j] not in ['X', 'O']:
                        # Simulate the AI move
                        board[i][j] = 'O'
                        score = self.evaluate_board(board, 'O')  # Heuristic score for AI
                        board[i][j] = None  # Undo the move

                        if score > best_score:
                            best_score = score
                            best_move = (i, j)

            # If no strategic move is found, pick a random available move
            if best_move:
                i, j = best_move
                board[i][j] = 'O'
            else:
                available_moves = [
                    (i, j) for i in range(5) for j in range(5) if board[i][j] not in ['X', 'O']
                ]
                if available_moves:
                    i, j = random.choice(available_moves)
                    board[i][j] = 'O'

        to_move = 'X'  # Switch turn back to the player

        # Render the board with the new move
        self.render_fivebyfive(board, self.X_IMG, self.O_IMG)
        pygame.display.update()

        return board, to_move

    def evaluate_board(self, board, player):
        """
        A simple heuristic evaluation function for the board.
        Gives a score based on potential lines of alignment.
        """
        opponent = 'X' if player == 'O' else 'O'
        score = 0

        # Check rows, columns, and diagonals for potential wins or blocks
        for i in range(5):
            score += self.evaluate_line([board[i][j] for j in range(5)], player, opponent)  # Row
            score += self.evaluate_line([board[j][i] for j in range(5)], player, opponent)  # Column

        # Check diagonals
        score += self.evaluate_line([board[i][i] for i in range(5)], player, opponent)  # Main diagonal
        score += self.evaluate_line([board[i][4 - i] for i in range(5)], player, opponent)  # Anti-diagonal

        return score

    def evaluate_line(self, line, player, opponent):
        """
        Evaluates a line (row, column, or diagonal) and returns a score.
        More aligned 'O's give positive scores, aligned 'X's give negative scores.
        """
        player_count = line.count(player)
        opponent_count = line.count(opponent)

        if player_count > 0 and opponent_count == 0:
            return player_count  # Positive score if AI has pieces and opponent has none
        elif opponent_count > 0 and player_count == 0:
            return -opponent_count  # Negative score if opponent has pieces and AI has none
        return 0  # Neutral score if both or none have pieces

    def check_win_fivebyfive(self, board):
        winner = None
        square_size = 772 // 5  # Each square is 154 pixels for a 5x5 board

        # Check rows for a win
        for row in range(5):
            if (board[row][0] == board[row][1] == board[row][2] == board[row][3] == board[row][4] 
                    and board[row][0] in ['X', 'O']):
                winner = board[row][0]
                for col in range(5):
                    winning_img = pygame.image.load(f"Graphics/Winning {winner}.png")
                    # Scale the image to fit the square
                    winning_img = pygame.transform.scale(winning_img, (square_size - 10, square_size - 10))
                    self.graphical_board[row][col][0] = winning_img
                    self.SCREEN.blit(self.graphical_board[row][col][0], self.graphical_board[row][col][1])
                pygame.display.update()
                return winner

        # Check columns for a win
        for col in range(5):
            if (board[0][col] == board[1][col] == board[2][col] == board[3][col] == board[4][col] 
                    and board[0][col] in ['X', 'O']):
                winner = board[0][col]
                for row in range(5):
                    winning_img = pygame.image.load(f"Graphics/Winning {winner}.png")
                    # Scale the image to fit the square
                    winning_img = pygame.transform.scale(winning_img, (square_size - 10, square_size - 10))
                    self.graphical_board[row][col][0] = winning_img
                    self.SCREEN.blit(self.graphical_board[row][col][0], self.graphical_board[row][col][1])
                pygame.display.update()
                return winner

        # Check main diagonal (top-left to bottom-right)
        if (board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] 
                and board[0][0] in ['X', 'O']):
            winner = board[0][0]
            for i in range(5):
                winning_img = pygame.image.load(f"Graphics/Winning {winner}.png")
                # Scale the image to fit the square
                winning_img = pygame.transform.scale(winning_img, (square_size - 10, square_size - 10))
                self.graphical_board[i][i][0] = winning_img
                self.SCREEN.blit(self.graphical_board[i][i][0], self.graphical_board[i][i][1])
            pygame.display.update()
            return winner

        # Check anti-diagonal (top-right to bottom-left)
        if (board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] 
                and board[0][4] in ['X', 'O']):
            winner = board[0][4]
            for i in range(5):
                winning_img = pygame.image.load(f"Graphics/Winning {winner}.png")
                # Scale the image to fit the square
                winning_img = pygame.transform.scale(winning_img, (square_size - 10, square_size - 10))
                self.graphical_board[i][4 - i][0] = winning_img
                self.SCREEN.blit(self.graphical_board[i][4 - i][0], self.graphical_board[i][4 - i][1])
            pygame.display.update()
            return winner

        # Check for a draw
        if all(board[i][j] in ['X', 'O'] for i in range(5) for j in range(5)):
            return "DRAW"

        return None
