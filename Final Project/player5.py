import math
import time
import random
import sys 

sys.setrecursionlimit(1500)

#increase or decrease to determine the amount of nodes to search before giving up and picking the best score. This affects how fast the code runs
cutoff = 600000

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        


    def get_move(self, game):
        valid_square = Falseval = None
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-24): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.lastmove = -1
        self.maxnodes = cutoff
        self.limit = False  #see if we hit our cutoff
        self.currnodes = 0  #total nodes recursed
        self.maxprune = 0   #number of max prunings
        self.minprune = 0   #number of min prunings
        self.turn = 0
        self.nextBestMove = {'position': None, 'score': 0}

    def get_move(self, game):
        if len(game.available_moves()) == 25:
            square = random.choice(game.available_moves())
        else:
            self.currnodes = 0  #reset value
            self.maxprune = 0   #reset value
            self.minprune = 0   #reset value
            self.nextBestMove = {'position': None, 'score': 0}
            t0 = time.time()
            square = self.minimax(game, self.letter)['position']
            t1 = time.time()
            if(self.currnodes > cutoff):
                print('Cutoff reached')
            print('The time minimax took to select a move:', t1-t0)
            print('Number of Nodes generated:', self.currnodes +1)
            print('Number of Max prunings: ', self.maxprune)
            print('Number of Min prunings: ', self.minprune)
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'
        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize

        if(self.currnodes < self.maxnodes):
            for possible_move in state.available_moves():
                state.make_move(possible_move, player)
                self.currnodes += 1
                
                sim_score = self.minimax(state, other_player)  # simulate a game after making that move

                # undo move
                state.board[possible_move] = ' '
                state.current_winner = None
                sim_score['position'] = possible_move  # this represents the move optimal next move

                if player == max_player:  # X is max player
                    if sim_score['score'] > best['score']:
                        self.maxprune += 1
                        best = sim_score
                else:
                    if sim_score['score'] < best['score']:
                        self.minprune += 1
                        best = sim_score
                        
        self.nextBestMove = best
        return self.nextBestMove
    

        