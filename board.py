import pygame
import sys

from checker_piece import checkerPiece
from checker_piece import update_position



# Initialisation de Pygame
pygame.init()



# Définition des couleurs
BLANC = (255, 255, 255)
BROWN = (67, 39, 15)


# Taille de la fenêtre et des cases du plateau
TAILLE_CASE = 80
LARGEUR = 8 * TAILLE_CASE
HAUTEUR = 8 * TAILLE_CASE

# Création de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu de Dames")



# Create a list to represent the initial arrangement of pieces on the board
initial_board = [
    [None, checkerPiece("brown"), None, checkerPiece("brown"), None, checkerPiece("brown"), None, checkerPiece("brown")],
    [checkerPiece("brown"), None, checkerPiece("brown"), None, checkerPiece("brown"), None, checkerPiece("brown"), None],
    [None, checkerPiece("brown"), None, checkerPiece("brown"), None, checkerPiece("brown"), None, checkerPiece("brown")],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [checkerPiece("black"), None, checkerPiece("black"), None, checkerPiece("black"), None, checkerPiece("black"), None],
    [None, checkerPiece("black"), None, checkerPiece("black"), None, checkerPiece("black"), None, checkerPiece("black")],
    [checkerPiece("black"), None, checkerPiece("black"), None, checkerPiece("black"), None, checkerPiece("black"), None],
]




# Fonction pour dessiner le plateau
def dessiner_plateau():
    for ligne in range(8):
        for colonne in range(8):
            couleur_case = BLANC if (ligne + colonne) % 2 == 0 else BROWN
            pygame.draw.rect(fenetre, couleur_case, (colonne * TAILLE_CASE, ligne * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

            piece = initial_board[ligne][colonne]
            if piece:
                piece_color = (16, 16, 16) if piece.color == "black" else (168, 113, 50)
                pygame.draw.circle(fenetre, piece_color, (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 2 - 5)

# Function to get valid moves for a checker piece
def get_valid_moves(board, row, col):
    valid_moves = []

    # Check if the square contains a checker
    if board[row][col] is not None:
        print(f"Piece present at ({row}, {col}): {type(board[row][col])}, color: {board[row][col].color}")

        # Check if it's an instance of checkerPiece with the correct color
        if isinstance(board[row][col], checkerPiece) and board[row][col].color == "black":
            print("Valid moves logic goes here for black pieces")

            # Add your logic for valid moves here
            if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] is None:
                valid_moves.append((row - 1, col - 1))
            if row - 1 >= 0 and col + 1 < len(board[0]) and board[row - 1][col + 1] is None:
                valid_moves.append((row - 1, col + 1))
        elif isinstance(board[row][col], checkerPiece) and board[row][col].color == "brown":
            print("Valid moves logic goes here for brown pieces")

            # Add your logic for valid moves for brown pieces here
            # Adjust the logic based on how brown pieces can move
            # For example, if brown pieces can move one square diagonally forward:
            if row + 1 < len(board) and col - 1 >= 0 and board[row + 1][col - 1] is None:
                valid_moves.append((row + 1, col - 1))
            if row + 1 < len(board) and col + 1 < len(board[0]) and board[row + 1][col + 1] is None:
                valid_moves.append((row + 1, col + 1))
        else:
            print("Not an instance of checkerPiece or wrong color")

    return valid_moves

# Function to draw valid move indicators
def draw_valid_moves(valid_moves):
    for move in valid_moves:
        pygame.draw.rect(fenetre, (0, 255, 0, 255), (move[1] * TAILLE_CASE, move[0] * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))



# Store the selected piece position
selected_piece = None

# Boucle principale du jeu
while True:
    dessiner_plateau()
    
    for event in pygame.event.get():
        
        mouse_x, mouse_y = pygame.mouse.get_pos()


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Convert pixel coordinates to board coordinates
            board_x = mouse_x // TAILLE_CASE
            board_y = mouse_y // TAILLE_CASE

            print("les positions de la case cliquée sont ", board_x, "et ", board_y)

    
             # Handle mouse click and update checker piece position
            if 0 <= board_y < len(initial_board) and 0 <= board_x < len(initial_board[0]):
                    if selected_piece is None:

                        # Select the checker piece if not already selected
                        selected_piece = (board_y, board_x)
                        valid_moves = get_valid_moves(initial_board, board_y, board_x)
                        print("Les mouvements valides sont :", valid_moves)
                        
                        

                    else:
                        # Move the selected checker piece to the clicked position
                        if (board_y, board_x) in valid_moves:
                            initial_board[board_y][board_x] = initial_board[selected_piece[0]][selected_piece[1]]
                            initial_board[selected_piece[0]][selected_piece[1]] = None
                            selected_piece = None
                           
                    draw_valid_moves(valid_moves)
                    pygame.time.delay(1000)  # Delay for 1000 milliseconds (1 second)

                    
    pygame.display.flip()



