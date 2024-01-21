from checker_piece import checkerPiece
#Création de nouvelle class
class King(checkerPiece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.is_king = True


        
