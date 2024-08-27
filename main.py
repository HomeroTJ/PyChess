from chessgame import *

def main() -> None:
    chessboard = Chessboard("rnbqkbnr/pppppppp/8/8/8/5p2/PPPPPPPP/RNBQKBNR" )
    chessboard.create_pieces()
    chessboard.print_board()
    # for piece in chessboard.pieces:
    #     if isinstance(piece, Pawn):
    #         print(piece.position, piece.canMove(chessboard.pieces))
    print(chessboard.read_move("Kg4+"))

            

if __name__ == "__main__":
    main()