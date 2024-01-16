from checker_piece import checkerPiece  


class Player:

    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur
        self.pions = []

    def initialiser_pions(self, plateau):
        for ligne in range(3):
            for colonne in range(8):
                if (ligne + colonne) % 2 == 1:
                    pion = Pion(self, ligne, colonne)
                    self.pions.append(pion)
                    plateau.set_pion(pion)













