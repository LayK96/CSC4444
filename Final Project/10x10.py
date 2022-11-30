import math
import time
from player10 import HumanPlayer, SmartComputerPlayer, RandomComputerPlayer


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(100)]

    def print_board(self):
        for row in [self.board[i*10:(i+1) * 10] for i in range(10)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*10, (j+1)*10)] for j in range(10)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 10)
        row = self.board[row_ind*10:(row_ind+1)*10]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 10
        column = [self.board[col_ind+i*10] for i in range(10)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 11 == 0:
            diagonal1 = [self.board[i] for i in [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
        if square % 9 == 0:
            diagonal2 = [self.board[i] for i in [9, 18, 27, 36,45,54,63,72,81,90]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)
    

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)