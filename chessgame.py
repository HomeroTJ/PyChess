import os

class Square():
    pass

class Pieces:
    def __init__(self, position: str, color: bool) -> None:
        self.position = position
        self.color = color

    def move(self):
        ...

class Pawn(Pieces):

    def get_rep(self):
        representation = "p"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()
        
    def canMove(self, other_pieces: list):
        """Returns a list of the posible squares that a piece can move"""
        if self.color == True:
            move_iter = 1
        if self.color == False:
            move_iter = -1

        possibles_moves = []
        
        column = ord(self.position[0])
        row = int(self.position[1])

        if row == 2 and self.color==True:
            possibles_moves.append(chr(column)+str(row+move_iter))
            possibles_moves.append(chr(column)+str(row+2*move_iter))
        
        if row == 7 and self.color==False:
            possibles_moves.append(chr(column)+str(row+move_iter))
            possibles_moves.append(chr(column)+str(row+2*move_iter))
        
        if self.color == False and row != 7:
            possibles_moves.append(chr(column)+str(row+move_iter))

        if self.color == True and row != 2:
            possibles_moves.append(chr(column)+str(row+move_iter))

        possible_attacks = []
        possible_attacks.append(chr(column-1)+str(row+move_iter))
        possible_attacks.append(chr(column+1)+str(row+move_iter))

        for piece in other_pieces:
            if piece.position in possible_attacks:
                possibles_moves.append(piece.position)
        
        return possibles_moves

            

class Bishop(Pieces):
    def get_rep(self):
        representation = "b"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()

class Rook(Pieces):
    def get_rep(self):
        representation = "r"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()

class Knight(Pieces):
    def get_rep(self):
        representation = "n"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()

class Queen(Pieces):
    def get_rep(self):
        representation = "q"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()

class King(Pieces):
    def get_rep(self):
        representation = "K"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()
        
class Chessboard():
    """Chesboard class"""
    std_initial_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR" 
    def __init__(
            self, 
            fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR",
            turn = "b",
            castle = "QKqk",
            enpassantTargets = "-",
            halfMoveCounter = 0,
            fullMoveCounter = 0) -> None:
        self.fen = fen
        self.turn = turn
        self.castle = castle
        self.enpassantTargets = enpassantTargets
        self.halfMoveCounter = halfMoveCounter
        self.fullMoveCounter = fullMoveCounter
        
    def create_pieces(self):
        map_pieces = {
            "p": Pawn,
            "P": Pawn,
            "n": Knight,
            "N": Knight,
            "n": Knight,        
            "r": Rook,
            "R": Rook,
            "b": Bishop,
            "B": Bishop,
            "q": Queen,
            "Q": Queen,
            "k": King,
            "K": King,
        }
        blackPieces = []
        whitePieces = []
        if self.turn == "w":
            initial_c = 1
            column = 1
            row = 8
            iter_c = 1
            iter_r = -1
        elif self.turn == "b":
            initial_c = 1
            column = 1
            row = 8
            iter_c = 1
            iter_r = -1
        else:
            return "Invalid Position! the second field on FEN string is not valid"

        for char in self.fen:
            if char.isalpha():
                if char.isupper():
                    pos_str = ""
                    pos_str += chr(int(97+column-1))
                    pos_str += str(row)
                    whitePieces.append(map_pieces[char](pos_str,True))
                    column += iter_c

                if char.islower():
                    pos_str = ""
                    pos_str += chr(97+column-1)
                    pos_str += str(row)
                    blackPieces.append(map_pieces[char](pos_str,False))
                    column += iter_c                
            
            if char.isnumeric():
                column += int(char)*iter_c

            if char == "/":
                column = initial_c
                row += iter_r

        self.pieces = whitePieces + blackPieces

    def read_move(self, move: str):
        
        if move[0].islower():
            for piece in self.pieces:
                if isinstance(piece,Pawn):
                    if move in piece.canMove():
                        print("si", piece.position)
        

    def print_board(self) -> None:
        """Prints the current position on terminal"""
        def print_row(num: int, color=int) -> None:
            for i in range(num):
                print(f"| {chrs[color]} ", end="")
                color = (color+1)%2

        def print_line_row() -> None:
            for i in range(8):
                print("----", end="")
            print("-")

        flag = 0
        pieces = [
            "r", "R",
            "n", "N",
            "b", "B",
            "k", "K",
            "q", "Q",
            "p", "P"
        ]
        chrs = {
        1: u'\u25FB',
        'P': u'\u265F',
        'R': u'\u265C',
        'N': u'\u265E',
        'B': u'\u265D',
        'K': u'\u265A',
        'Q': u'\u265B',
        0: u'\u25FC',
        'p': u'\u2659',
        'r': u'\u2656',
        'n': u'\u2658',
        'b': u'\u2657',
        'k': u'\u2654',
        'q': u'\u2655'
        }
        

        os.system('cls')
        print_line_row()

        color = 0

        if self.turn == "w":
            position = self.fen
        elif self.turn == "b":
            position = self.fen[::-1]

        for character in position:
            if character in pieces:
                print(f"| {chrs[character]} ", end="")
                color = (color+1)%2
            elif character == "/":
                print("|")
                flag = 1
                print_line_row()
                color = (color+1)%2
            elif (character.isnumeric()):
                print_row(int(character), color)
                flag = 0
                color = (color+int(character))%2

            
            
        print("|")
        print_line_row()
    
    def read_move(self, move: str):
        """Takes as input a chess move in algebraic notation an updates the fenstring to make it"""
        ### Here obtains the target square to move a piece
        square_to_move = ""
        map_pieces = {
            "p": Pawn,
            "P": Pawn,
            "n": Knight,
            "N": Knight,
            "n": Knight,        
            "r": Rook,
            "R": Rook,
            "b": Bishop,
            "B": Bishop,
            "q": Queen,
            "Q": Queen,
            "k": King,
            "K": King,
        }


        for i in range(0,len(move)):
            if move[::-1][i].isnumeric():
                square_to_move += move[::-1][i]
            if move[::-1][i].islower():
                square_to_move += move[::-1][i]
                break 

        square_to_move = square_to_move[::-1]

        if move[0].islower():
            actual_piece = Pawn
        else:
            actual_piece = map_pieces[move[0]]


        col = 0
        row = 0
        for letter in self.fen:
            if letter.isnumeric():
                col += int(letter)

        return square_to_move
