class checkerPiece:
    
    def __init__(self, color):
        self.color = color
        self.is_king = False

    def promote_to_king(self):
        self.is_king = True


        