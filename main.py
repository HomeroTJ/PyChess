from chessgame import *

def main() -> None:
    chessboard = Chessboard()
    chessboard.create_pieces()
    chessboard.print_board()

    while True:
        chessboard.read_move(input("Ingrese un movimiento: "))
        chessboard.update_fen()
        chessboard.print_board()

    # chessboard.read_move(("e4"))
    # chessboard.update_fen()
    # chessboard.print_board()
    # chessboard.read_move(("e5"))
    # chessboard.update_fen()
    # chessboard.print_board()
    # chessboard.read_move(("f4"))
    # chessboard.update_fen()
    # chessboard.print_board()
    # chessboard.read_move(("Qh4"))
    # chessboard.update_fen()
    # chessboard.print_board()
    # for piece in chessboard.pieces:
    #     if isinstance(piece, King):
    #         print(piece.is_checked(chessboard.pieces),piece.position)

if __name__ == "__main__":
    main()