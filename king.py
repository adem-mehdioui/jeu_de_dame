from checker_piece import checkerPiece

class King (checkerPiece):
    def __init__(self, joueur, ligne, colonne):
        super().__init__(joueur, ligne, colonne)
        self.est_dame = False

        
