class checkerPiece:
    
    def __init__(self, color):
        self.color = color
        self.is_king = False

    def promote_to_king(self):
        self.is_king = True



    def update_position(self, new_row, new_col):
        self.row = new_row
        self.col = new_col


        