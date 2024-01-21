import pygame
import sys

from checker_piece import checkerPiece
from checker_piece import update_position



# Initialisation de Pygame
pygame.init()



# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)


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
    [checkerPiece("red"), None, checkerPiece("red"), None, checkerPiece("red"), None, checkerPiece("red"), None],
    [None, checkerPiece("red"), None, checkerPiece("red"), None, checkerPiece("red"), None, checkerPiece("red")],
    [checkerPiece("red"), None, checkerPiece("red"), None, checkerPiece("red"), None, checkerPiece("red"), None],
]




# Fonction pour dessiner le plateau
def dessiner_plateau():
    for ligne in range(8):
        for colonne in range(8):
            couleur_case = BLANC if (ligne + colonne) % 2 == 0 else NOIR
            pygame.draw.rect(fenetre, couleur_case, (colonne * TAILLE_CASE, ligne * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

            piece = initial_board[ligne][colonne]
            if piece:
                piece_color = (255, 0, 0) if piece.color == "red" else (168, 113, 50)
                pygame.draw.circle(fenetre, piece_color, (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 2 - 5)



