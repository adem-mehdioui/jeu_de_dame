import pygame
import sys
from player import Player
from checker_piece import checkerPiece


# Define players
brown_player = Player("brown")
black_player = Player("black")

# Define initial player
current_player = black_player

print(f"{current_player.name} turn")





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
        if isinstance(board[row][col], checkerPiece):
            # Define the directions to check for capturing moves
            capture_directions = [(1, -1), (1, 1)] if board[row][col].color == "brown" else [(-1, -1), (-1, 1)]

            for dir_row, dir_col in capture_directions:
                capture_row = row + dir_row
                capture_col = col + dir_col
                target_row = row + 2 * dir_row
                target_col = col + 2 * dir_col

                # Check if the capturing move is within bounds
                if 0 <= target_row < len(board) and 0 <= target_col < len(board[0]):
                    # Check if the target square is empty and the intermediate square has an opponent checker piece
                    if board[capture_row][capture_col] is not None and board[capture_row][capture_col].color != board[row][col].color and board[target_row][target_col] is None:
                        valid_moves.append((target_row, target_col))

            # Add your logic for valid moves here
            if board[row][col].color == "black":
                if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] is None:
                    valid_moves.append((row - 1, col - 1))
                if row - 1 >= 0 and col + 1 < len(board[0]) and board[row - 1][col + 1] is None:
                    valid_moves.append((row - 1, col + 1))
                if row == 0:
                    board[row][col].promote_to_king()
                    print(f"The checker piece at ({row}, {col}) is in the first row.")
            elif board[row][col].color == "brown":
                if row + 1 < len(board) and col - 1 >= 0 and board[row + 1][col - 1] is None:
                    valid_moves.append((row + 1, col - 1))
                if row + 1 < len(board) and col + 1 < len(board[0]) and board[row + 1][col + 1] is None:
                    valid_moves.append((row + 1, col + 1))
                if row == len(board) - 1:
                    board[row][col].promote_to_king()
                
        else:
            print("Not an instance of checkerPiece")

    print("Valid moves:", valid_moves)
    return valid_moves




# Function to draw valid move indicators as white balls
def draw_valid_moves(valid_moves):
    for move in valid_moves:
        pygame.draw.circle(
            fenetre,  # Surface to draw on
            (255, 255, 255),  # Color of the circle (white in RGB)
            (move[1] * TAILLE_CASE + TAILLE_CASE // 2, move[0] * TAILLE_CASE + TAILLE_CASE // 2),  # Center coordinates
            TAILLE_CASE // 4 - 5  # Radius of the circle
        )


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

            

            # Handle mouse click and update checker piece position
            if 0 <= board_y < len(initial_board) and 0 <= board_x < len(initial_board[0]):
                
                    piece = initial_board[board_y][board_x]

                    if piece and piece.color == current_player.name:
                        # Select the checker piece if not already selected
                        selected_piece = (board_y, board_x)
                        valid_moves = get_valid_moves(initial_board, board_y, board_x)


                         # Check if there are capturing moves
                        capturing_moves = [move for move in valid_moves if abs(move[0] - selected_piece[0]) == 2]

                        
                        if capturing_moves:
                            valid_moves = capturing_moves  # Restrict to capturing moves only


    # Draw the valid moves continuously
    if selected_piece is not None:
            draw_valid_moves(valid_moves)
                        

                        
                    # Move the selected checker piece to the clicked position
            if (board_y, board_x) in valid_moves:

                            capturing_moves = [move for move in valid_moves if abs(move[0] - selected_piece[0]) == 2]

                            if capturing_moves:

                                # Perform the deletion of the captured pawn here
                                for move in capturing_moves:
                                    capture_row, capture_col = (
                                        (selected_piece[0] + move[0]) // 2,
                                        (selected_piece[1] + move[1]) // 2,
                                    )

                                    # Remove the captured piece from the board
                                    initial_board[capture_row][capture_col] = None

                                initial_board[board_y][board_x] = initial_board[selected_piece[0]][selected_piece[1]]
                                initial_board[selected_piece[0]][selected_piece[1]] = None
                                selected_piece = None
                                current_player = black_player if current_player == brown_player else brown_player  # Switch turns
                                print(f"{current_player.name} turn")


                                



                            else: 

                                # Regular move, the target square is empty
                                initial_board[board_y][board_x] = initial_board[selected_piece[0]][selected_piece[1]]
                                initial_board[selected_piece[0]][selected_piece[1]] = None
                                selected_piece = None
                                current_player = black_player if current_player == brown_player else brown_player  # Switch turns
                                print(f"{current_player.name} turn")

              

                                

    pygame.display.flip()


    
     

