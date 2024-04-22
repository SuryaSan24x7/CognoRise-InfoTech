import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(WHITE)

# Define the board
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Define constants for the players
X = 'X'
O = 'O'
EMPTY = None

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(BOARD_ROWS):
        if all([board[i][j] == player for j in range(BOARD_COLS)]) or \
           all([board[j][i] == player for j in range(BOARD_ROWS)]):
            return True
    if all([board[i][i] == player for i in range(BOARD_ROWS)]) or \
       all([board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS)]):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([cell is not EMPTY for row in board for cell in row])

# Function to get the available moves
def get_available_moves(board):
    available_moves = []
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] == EMPTY:
                available_moves.append((i, j))
    return available_moves

# Minimax algorithm
def minimax(board, depth, maximizing_player):
    if check_winner(board, X):
        return -1
    elif check_winner(board, O):
        return 1
    elif is_board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = -math.inf
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = O
            eval = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = X
            eval = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

# Function to get the best move using minimax
def get_best_move(board):
    best_eval = -math.inf
    best_moves = []
    for move in get_available_moves(board):
        i, j = move
        board[i][j] = O
        eval = minimax(board, 0, False)
        board[i][j] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_moves = [move]
        elif eval == best_eval:
            best_moves.append(move)
    return random.choice(best_moves)

# Function to draw the grid lines
def draw_grid():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw the X and O on the board
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == X:
                pygame.draw.line(screen, GREEN, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, GREEN, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + SQUARE_SIZE - 20),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + 20), LINE_WIDTH)
            elif board[row][col] == O:
                pygame.draw.circle(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 20, LINE_WIDTH)

# Function to get row and column from mouse click
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Function to display whose turn it is
def show_turn(player):
    font = pygame.font.SysFont(None, 48)
    text = font.render(f"Player {player}'s turn", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

# Main game loop
def main():
    current_player = X
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_player == X:
                    row, col = get_row_col_from_mouse(event.pos)
                    if board[row][col] is None:
                        board[row][col] = X
                        if check_winner(board, X):
                            print("Player wins!")
                            game_over = True
                        elif is_board_full(board):
                            print("It's a tie!")
                            game_over = True
                        else:
                            current_player = O
                else:  # AI's turn
                    best_move = get_best_move(board)
                    board[best_move[0]][best_move[1]] = O
                    if check_winner(board, O):
                        print("AI wins!")
                        game_over = True
                    elif is_board_full(board):
                        print("It's a tie!")
                        game_over = True
                    else:
                        current_player = X

        screen.fill(WHITE)
        draw_grid()
        draw_figures()
        show_turn(current_player)
        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()
