from colorama import Fore, Back, Style

class Board:
    def __init__(self):
        self.grid = self.create_starting_board()
        
    def create_starting_board(self):
        # Create empty 8x8 grid
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Set up pawns
        for col in range(8):
            board[1][col] = '♟'  # Black pawn
            board[6][col] = '♙'  # White pawn
            
        # Set up other pieces
        pieces = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
        for col, piece in enumerate(pieces):
            board[0][col] = piece  # Black pieces
            board[7][col] = piece.upper()  # White pieces
            
        return board

    def display(self):
        print("\n  a b c d e f g h")
        for row_idx, row in enumerate(self.grid):
            print(8 - row_idx, end=' ')
            for col_idx, piece in enumerate(row):
                color = Back.GREEN if (row_idx + col_idx) % 2 else Back.YELLOW
                piece = piece or ' '
                print(f"{color}{Fore.BLACK if piece.islower() else Fore.WHITE} {piece}{Style.RESET_ALL}", end='')
            print(f" {8 - row_idx}")
        print("  a b c d e f g h\n")

    def move_piece(self, start, end, player):
        start_row, start_col = start
        end_row, end_col = end
        
        piece = self.grid[start_row][start_col]
        target_piece = self.grid[end_row][end_col]
        
        # Basic validation
        if not piece:
            return False
        if player == 'white' and piece.islower():
            return False
        if player == 'black' and piece.isupper():
            return False
        if target_piece and ((target_piece.islower() and player == 'black') or 
                           (target_piece.isupper() and player == 'white')):
            return False
            
        # Basic move validation (just checks if space is empty or contains opponent's piece)
        self.grid[end_row][end_col] = piece
        self.grid[start_row][start_col] = None
        return True
