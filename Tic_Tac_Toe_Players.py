import math
import random

class Player:
    def __init__(self,letter):
        # The letter can be x or o
        self.letter = letter

    # The player can get his/her move
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # Choosing a random valid cell for the next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-8): ')
            # Checking if this is a correct value by casting it into an integer, if its not or if the cell is not available we say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                # If the value is correct then it is accepted
                valid_square = True 
            except ValueError:
                print('Invalid square. Try again.')
        return val
    
class MinMaxComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        # If the board is empty then pick a random cell
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        # Else choose a cell based on the minmax algorithm
        else:
            square = self.minmax(game, self.letter)['position']
            return square
    
    def minmax(self, state, player):
        # This is us
        max_player = self.letter
        # This is the opponent
        other_player = 'O' if player == 'X' else 'X'

        #Checking if the previous move won the game
        if state.current_winner == other_player:
            # Returning the position and score
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        
        # Checking if there are no emepty squares
        elif not state.empty_squares():
            return{'position': None, 'score': 0}
        
        if player == max_player:
            # Each score should maximize
            best = {'position': None, 'score': -math.inf}
        else:
            # Each score should minimize
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # Trying a move
            state.make_move(possible_move, player)

            # Recurse using minmax to simulate a game after making that move
            sim_score = self.minmax(state, other_player)

            # Undo the move after checking
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # Update the maximizer and the minimizer if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best