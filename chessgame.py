'''
Welcome to this project of my own, a python library called (add a cool name here)
the purpouse of this project is to develop a python library that can handle
information of a chess game, also working as a game engine for a chess game.

The future for this project is make a native way to handle chess data on python
'''

import os

class Square():
    pass

class Pieces:
    """This is the parent class of all the pieces, all pieces
    have minimum these two methods"""
    def __init__(self, position: str, color: bool) -> None:
        self.position = position #Contains the square where is the piece
        self.color = color #True if the color is white, False if the color is black

    def get_rep(self):
        """Returns the representation of the piece to build later the FEN string"""
        ...

    def can_move(self, other_pieces):
        """Returns a list of all the posible moves of a piece"""
        ...

class Pawn(Pieces):

    def get_rep(self) -> str:
        representation = "p"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()
        
    def can_attack(self, other_pieces: list) -> list:
        """This function returns the squares of a piece that a pawn can eat"""

        # MUST IMPLEMENT ENPASSANT

        #Depending on the color of the piece, we give a different value to the iteration value
        #this is because we use a global coordinate system for the squares

        if self.color == True:
            move_iter = 1
        if self.color == False:
            move_iter = -1

        #we store the column and the row (in an integer variable) where is the pawn
        column = ord(self.position[0])
        row = int(self.position[1])

        possible_attacks = []
        
        #This loop iterates over all the pieces on the board and checks if they are in a square where
        #a pawn can take a piece, then, return all the squares on a list
        for piece in other_pieces:
            if (piece.position == chr(column-1)+str(row+move_iter)) and (piece.color != self.color):
                possible_attacks.append(chr(column-1)+str(row+move_iter))
            elif (piece.position == chr(column+1)+str(row+move_iter)) and (piece.color != self.color):
                possible_attacks.append(chr(column+1)+str(row+move_iter))

        return possible_attacks
        
    def can_move(self, other_pieces: list) -> list:
        """Returns a list of the posible squares that a piece can move"""

        #Depending on the color of the piece, we give a different value to the iteration value
        #this is because we use a global coordinate sistem for the squares
        if self.color == True:
            move_iter = 1
        if self.color == False:
            move_iter = -1

        possibles_moves = []
        
        #We storage the column an the row of the pawn in an integer variable
        column = ord(self.position[0])
        row = int(self.position[1])

        #Here passes different conditions to make the different cases where a pawn can be
        # 
        # Must implement queening
        #

        if (row == 2) and (self.color==True):
            piece_on_square = [other.position for other in other_pieces if (other.position ==chr(column)+str(row+move_iter)) or (other.position ==chr(column)+str(2*row+move_iter))]
            if not(chr(column)+str(row+move_iter) in piece_on_square):
                possibles_moves.append(chr(column)+str(row+move_iter))
            if not(chr(column)+str(row+2*move_iter) in piece_on_square):
                possibles_moves.append(chr(column)+str(row+2*move_iter))
        
        if row == 7 and self.color==False:
            piece_on_square = [other.position for other in other_pieces if (other.position ==chr(column)+str(row+move_iter)) or (other.position ==chr(column)+str(2*row+move_iter))]
            if not(chr(column)+str(row+move_iter) in piece_on_square):
                possibles_moves.append(chr(column)+str(row+move_iter))
            if not(chr(column)+str(row+2*move_iter) in piece_on_square):
                possibles_moves.append(chr(column)+str(row+2*move_iter))
        
        if self.color == False and row != 7:
            piece_on_square = [other.position for other in other_pieces if (other.position ==chr(column)+str(row+move_iter))]
            if not(chr(column)+str(row+move_iter) in piece_on_square):
                possibles_moves.append(chr(column)+str(row+move_iter))

        if self.color == True and row != 2:
            piece_on_square = [other.position for other in other_pieces if (other.position ==chr(column)+str(row+move_iter))]
            if (chr(column)+str(row+move_iter) in piece_on_square):
                pass
            else:
                possibles_moves.append(chr(column)+str(row+move_iter))
            

        possible_attacks = []
        possible_attacks.append(chr(column-1)+str(row+move_iter))
        possible_attacks.append(chr(column+1)+str(row+move_iter))

        for piece in other_pieces:
            if (piece.position in possible_attacks) and piece.color != self.color:
                possibles_moves.append(piece.position)

        return possibles_moves

            

class Bishop(Pieces):
    def get_rep(self) -> str:
        representation = "b"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()
        
    def can_move(self, other_pieces):
        posible_moves = []

        column = ord(self.position[0])
        row = int(self.position[1])        

        iter_col = [-1,1]
        iter_row = [-1,1]


        for change_col in iter_col:
            for change_row in iter_row:
                itering_col = column
                itering_row = row

                while True:
                    itering_col += change_col
                    itering_row += change_row

                    if ((itering_col > ord("h")) or (itering_col < ord("a"))) or ((itering_row > 8) or (itering_row < 1)):
                        break

                    piece_on_square = [piece for piece in other_pieces if piece.position == chr(itering_col)+str(itering_row)]

                    if len(piece_on_square) == 0:
                        posible_moves.append(chr(itering_col)+str(itering_row))
                    else:
                        for piece in piece_on_square:
                            if piece.color != self.color:
                                posible_moves.append(chr(itering_col)+str(itering_row))
                                break
                        break

        return posible_moves
class Rook(Pieces):
    def get_rep(self) -> str:
        representation = "r"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()
        
    def can_move(self, other_pieces):
        posible_moves = []

        iter_col = [-1,1]
        iter_row = [-1,1]

        column = ord(self.position[0])
        row = int(self.position[1]) 

        for change_col in iter_col:
                itering_col = column
                itering_row = row

                while True:
                    itering_col += change_col

                    if ((itering_col > ord("h")) or (itering_col < ord("a"))):
                        break

                    piece_on_square = [piece for piece in other_pieces if piece.position == chr(itering_col)+str(itering_row)]

                    if len(piece_on_square) == 0:
                        posible_moves.append(chr(itering_col)+str(itering_row))
                    else:
                        for piece in piece_on_square:
                            if piece.color != self.color:
                                posible_moves.append(chr(itering_col)+str(itering_row))
                                break
                        break
                        
        for change_row in iter_row:
                itering_col = column
                itering_row = row

                while True:
                    itering_row += change_row

                    if ((itering_row > 8) or (itering_row < 1)):
                        break

                    piece_on_square = [piece for piece in other_pieces if piece.position == chr(itering_col)+str(itering_row)]

                    if len(piece_on_square) == 0:
                        posible_moves.append(chr(itering_col)+str(itering_row))
                    else:
                        for piece in piece_on_square:
                            if piece.color != self.color:
                                posible_moves.append(chr(itering_col)+str(itering_row))
                                break
                        break

        return posible_moves

class Knight(Pieces):
    def get_rep(self) -> str:
        representation = "n"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()
        
    def can_move(self, other_pieces):
        posible_moves = []

        column = ord(self.position[0])
        row = int(self.position[1]) 

        change_on_coord = [
            (1,2), (1,-2),
            (2,1), (2,-1),
            (-1,2),(-1,-2),
            (-2,1),(-2,-2),
        ]

        for tuple in change_on_coord:
            itering_col = column + tuple[0]
            itering_row = row + tuple[1]

            if not(((itering_col > ord("h")) or (itering_col < ord("a"))) or ((itering_row > 8) or (itering_row < 1))):
                piece_on_square = [piece for piece in other_pieces if piece.position == chr(itering_col)+str(itering_row)]

                if len(piece_on_square) == 0:
                    posible_moves.append(chr(itering_col)+str(itering_row))
                else:
                    for piece in piece_on_square:
                        if piece.color != self.color:
                            posible_moves.append(chr(itering_col)+str(itering_row))
                            
        return posible_moves

class Queen(Pieces):
    def get_rep(self) -> str:
        representation = "q"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()
    
    def can_move(self, other_pieces):
        posible_moves = []

        iter_col = [-1,1]
        iter_row = [-1,1]

        column = ord(self.position[0])
        row = int(self.position[1]) 

        for change_col in iter_col:
                itering_col = column
                itering_row = row

                while True:
                    itering_col += change_col

                    if ((itering_col > ord("h")) or (itering_col < ord("a"))):
                        break

                    piece_on_square = [piece for piece in other_pieces if piece.position == chr(itering_col)+str(itering_row)]

                    if len(piece_on_square) == 0:
                        posible_moves.append(chr(itering_col)+str(itering_row))
                    else:
                        for piece in piece_on_square:
                            if piece.color != self.color:
                                posible_moves.append(chr(itering_col)+str(itering_row))
                                break
                        break
                        
        for change_row in iter_row:
                itering_col = column
                itering_row = row

                while True:
                    itering_row += change_row

                    if ((itering_row > 8) or (itering_row < 1)):
                        break

                    piece_on_square = [piece for piece in other_pieces if piece.position == chr(itering_col)+str(itering_row)]

                    if len(piece_on_square) == 0:
                        posible_moves.append(chr(itering_col)+str(itering_row))
                    else:
                        for piece in piece_on_square:
                            if piece.color != self.color:
                                posible_moves.append(chr(itering_col)+str(itering_row))
                                break
                        break

        column = ord(self.position[0])
        row = int(self.position[1])        

        iter_col = [-1,1]
        iter_row = [-1,1]

        for change_col in iter_col:
            for change_row in iter_row:
                itering_col = column
                itering_row = row

                while True:
                    itering_col += change_col
                    itering_row += change_row

                    if ((itering_col > ord("h")) or (itering_col < ord("a"))) or ((itering_row > 8) or (itering_row < 1)):
                        break

                    piece_on_square = [piece for piece in other_pieces if piece.position == chr(itering_col)+str(itering_row)]

                    if len(piece_on_square) == 0:
                        posible_moves.append(chr(itering_col)+str(itering_row))
                    else:
                        for piece in piece_on_square:
                            if piece.color != self.color:
                                posible_moves.append(chr(itering_col)+str(itering_row))
                                break
                        break

        return posible_moves

class King(Pieces):
    def get_rep(self) -> str:
        representation = "K"
        if self.color:
            return representation.upper()
        else:
            return representation.lower()
        
    def can_move(self, other_pieces):
        posible_moves = []

        column = ord(self.position[0])
        row = int(self.position[1]) 

        change_in_col = [0,1,-1]
        change_in_row = [0,1,-1]

        for change_x in change_in_row:
            for change_y in change_in_col:
            
                itering_col = column + change_y
                itering_row = row + change_x

                if (change_in_col == 0) and (change_in_row == 0):
                    pass

                else:
                    if not(((itering_col > ord("h")) or (itering_col < ord("a"))) or ((itering_row > 8) or (itering_row < 1))):
                        piece_on_square = [piece for piece in other_pieces if piece.position == chr(itering_col)+str(itering_row)]

                        if len(piece_on_square) == 0:
                            posible_moves.append(chr(itering_col)+str(itering_row))
                        else:
                            for piece in piece_on_square:
                                if piece.color != self.color:
                                    posible_moves.append(chr(itering_col)+str(itering_row))

        return posible_moves
    
    

    

    
    def is_checked(self, other_pieces: list):
        enemy_pieces = [pieces for pieces in other_pieces if (pieces.color != self.color)]

        for enemy in enemy_pieces:
            check = enemy.can_move(other_pieces)
            if self.position in check:
                return True
            
        return False

class Chessboard():
    """Chesboard class"""
    std_initial_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR" 
    def __init__(
            self, 
            fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR",
            turn = "w",
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
        flag = 0
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

        map_turn = {
            "w": True,
            "b": False
        }

        map_iteration = {
            True: 1,
            False: 2
        }
        
        # for i in range(0,len(move)):
        #     if move[::-1][i].isnumeric():
        #         square_to_move += move[::-1][i]
        #     if move[::-1][i].islower():
        #         square_to_move += move[::-1][i]
        #         break 

        # square_to_move = square_to_move[::-1]
        square_to_move = move[::-1][0:2][::-1]

        if move[0].islower():
            actual_piece = Pawn

        ### The following piece of code make sure that the short castle is a valid move, it it is, it is done and updated

        elif move == "O-O":
            map_castle = {
                True: "K",
                False: "k"
            }
            map_position = {
                True: ("e1","h1"),
                False: ("e8","h8")
            }

            for piece in self.pieces:
                if (isinstance(piece,King)) and (piece.color == map_turn[self.turn]):
                    column = ord(piece.position[0])
                    row = int(piece.position[1]) 

                    enemy_pieces = [piecenem for piecenem in self.pieces if piece.color != piecenem.color]
                    enemy_squares = set()

                    for enemy in enemy_pieces:
                        for square in enemy.can_move(self.pieces):
                            enemy_squares.add(square)

                    if piece.is_checked(self.pieces):
                        return self.read_move(str(input("Please enter a valid move, the king is checked: ")))
                    elif not(map_castle[piece.color] in self.castle):
                        return self.read_move(str(input("Please enter a valid move, castling is not available: ")))
                    elif piece.position != map_position[piece.color][0]:
                        return self.read_move(str(input("Please enter a valid move, king not on his place: ")))
                    
                    rooks = [rook for rook in self.pieces if (isinstance(rook,Rook)) and (rook.position == map_position[piece.color][1])]

                    if len(rooks) != 1:
                        return self.read_move(str(input("Please enter a valid move: ")))
                    
                    for index in range(2):
                        column += 1
                        if (chr(column)+str(row) in enemy_squares):
                            return self.read_move(str(input("Please enter a valid move: ")))
                        
                        checking_pieces = [pix for pix in self.pieces if (pix.color == piece.color) and (pix.position == (chr(column)+str(row)))]

                        if len(checking_pieces) != 0:
                            return self.read_move(str(input("Please enter a valid move: ")))
                        
                    piece.position = chr(column)+str(row)
                    rooks[0].position = chr(column-1)+str(row)
                    
                    return
        ### this piece of code checks if the long castle is a valid move and if it is, then it is done
        elif move == "O-O-O":     
            map_castle = {
                True: "Q",
                False: "q"
            }
            map_position = {
                True: ("e1","a1"),
                False: ("e8","a8")
            }
            for piece in self.pieces:
                if (isinstance(piece,King)) and (piece.color == map_turn[self.turn]):
                    column = ord(piece.position[0])
                    row = int(piece.position[1]) 

                    enemy_pieces = [piecenem for piecenem in self.pieces if piece.color != piecenem.color]
                    enemy_squares = set()

                    for enemy in enemy_pieces:
                        for square in enemy.can_move(self.pieces):
                            enemy_squares.add(square)

                    if piece.is_checked(self.pieces):
                        return self.read_move(str(input("Please enter a valid move, the king is checked: ")))
                    elif not(map_castle[piece.color] in self.castle):
                        return self.read_move(str(input("Please enter a valid move, castling is not available: ")))
                    elif piece.position != map_position[piece.color][0]:
                        return self.read_move(str(input("Please enter a valid move, king not on his place: ")))
                    
                    rooks = [rook for rook in self.pieces if (isinstance(rook,Rook)) and (rook.position == map_position[piece.color][1])]

                    if len(rooks) != 1:
                        return self.read_move(str(input("Please enter a valid move: ")))
                    
                    for index in range(3):
                        column -= 1
                        if (chr(column)+str(row) in enemy_squares) and index < 2:
                            return self.read_move(str(input("Please enter a valid move: ")))
                        
                        checking_pieces = [pix for pix in self.pieces if (pix.color == piece.color) and (pix.position == (chr(column)+str(row)))]

                        if len(checking_pieces) != 0:
                            return self.read_move(str(input("Please enter a valid move: ")))
                        
                    piece.position = chr(column+1)+str(row)
                    rooks[0].position = chr(column+2)+str(row)
                    
                    return       


        ### This section of the code handles every othe move
        ### first take 
        else:
            actual_piece = map_pieces.get(move[0],0)

        pieces_to_check = [] #Here we would store the pieces that can make the move that it read
        piece_on_square = []
        for piece in self.pieces:
            if piece.position == square_to_move:
                piece_on_square.append(piece)
            if isinstance(piece, actual_piece):
                if (square_to_move in piece.can_move(self.pieces)) and map_turn[self.turn] == piece.color:
                    pieces_to_check.append(piece)
        
        if (len(piece_on_square)>0 and not('x' in move)):
            return self.read_move(str(input('Captures must be indicated with an x. Please enter a valid move: ')))

        if len(pieces_to_check) == 1:
            map_position = {
                True: ("a1","h1"),
                False: ("a8","h8")
            }
            
            if isinstance(pieces_to_check[0],Rook) and (pieces_to_check[0].position in map_position[pieces_to_check[0].color]):
                
                if pieces_to_check[0].position == 'a1' and ('Q' in self.castle):
                    self.castle = self.castle.replace('Q', '')
                if pieces_to_check[0].position == 'h1' and ('K' in self.castle):
                    self.castle = self.castle.replace('K', '')
                if pieces_to_check[0].position == 'a8' and ('Q' in self.castle):
                    self.castle = self.castle.replace('q', '')
                if pieces_to_check[0].position == 'h8' and ('K' in self.castle):
                    self.castle = self.castle.replace('k', '')
                

            pieces_to_check[0].position = square_to_move
            flag = 1
            

        ### This handles the case where two pieces can make the move
        if len(pieces_to_check) > 1:
            move_to_check = move[:-2]
            for piece in pieces_to_check:
                if (piece.position in move_to_check) or (piece.position[0] in move_to_check):
                    piece.position = square_to_move
                    flag = 1
                    if isinstance(piece,Rook) and piece.position in map_position[piece.color]:
                        if piece.position == 'a1' and 'Q' in self.castle:
                            self.castle.replace('Q', '')
                        if piece.position == 'h1' and 'K' in self.castle:
                            self.castle.replace('K', '')
                        if piece.position == 'a8' and 'Q' in self.castle:
                            self.castle.replace('q', '')
                        if piece.position == 'h8' and 'K' in self.castle:
                            self.castle.replace('k', '')
                
        if flag == 0:
            print("Thats not a valid move")
            return self.read_move(str(input("Please enter a valid move: ")))

        if "x" in move: #This runs if the move is a capture only eliminates the destination piece of where it is going
            if move[0].islower():
                actual_piece = Pawn
            else:
                actual_piece = map_pieces[move[0]]

            for i in range(len(move)):
                if move[i] == "x":
                    move_dummy = move[i+1:i+3]
                    self.pieces = [piece for piece in self.pieces if  not ((piece.position == move_dummy) and piece.color != map_turn[self.turn])]
        
        for piece in self.pieces:
            if isinstance(piece, King) and (piece.color == map_turn[self.turn]):
                enemy_pieces = [pieces for pieces in self.pieces if (pieces.color != piece.color)]
                
                if piece.is_checked(self.pieces):
                    # Chessboard.create_pieces()

                    # ally_pieces = [pieces for pieces in self.pieces if (pieces.color == piece.color)]

                    # for ally in ally_pieces:
                    #     for pos in ally.can
                        

                    return self.read_move(str(input("Please enter a valid move: ")))
                
        return

    
    def update_fen(self):
        map_change = {"w":"b", "b":"w"}

        self.turn=map_change[self.turn]

        new_fen = ""
        for row in range(7,-1,-1):
            acum_squares = 0
            for col in range(8):
                actual_square = chr(int(97+col)) + str(row + 1)
                for piece in self.pieces:
                    if piece.position == actual_square:
                        if acum_squares > 0:
                            new_fen += str(acum_squares)
                            acum_squares = 0
                        new_fen += piece.get_rep()
                        acum_squares = -1
                acum_squares += 1

                if col == 7 and acum_squares > 0:
                    new_fen += str(acum_squares)

            
            if row >0:
                new_fen += "/"

        self.fen = new_fen
