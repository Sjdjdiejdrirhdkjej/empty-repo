from chess.board import Board
from colorama import Fore, Style

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'white'

    def play(self):
        while True:
            self.board.display()
            print(f"{self.current_player.capitalize()}'s turn")
            move = input("Enter move (e.g. 'e2 e4'): ")
            
            if self.make_move(move):
                self.current_player = 'black' if self.current_player == 'white' else 'white'
            else:
                print("Invalid move - try again")

    def make_move(self, move):
        try:
            start, end = move.split()
            start_pos = self.parse_position(start)
            end_pos = self.parse_position(end)
            
            if self.board.move_piece(start_pos, end_pos, self.current_player):
                return True
            return False
        except:
            return False

    def parse_position(self, pos):
        col = ord(pos[0].lower()) - ord('a')
        row = 8 - int(pos[1])
        return (row, col)
