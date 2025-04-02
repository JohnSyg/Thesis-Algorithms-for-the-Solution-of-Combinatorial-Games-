import time
from Tic_Tac_Toe_Players import HumanPlayer, RandomComputerPlayer, MinMaxComputerPlayer

class TicTacToe:
    def __init__(self):
        # Using a single list to reprisent a 3x3 board
        self.board = [' ' for _ in range(9)]
        # Keeping track of the winner
        self.current_winner = None


    def print_board(self):
        # Split the three rows depending on the value of i
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            # Printing the rows as one string
            print ('| ' +  ' | '.join(row) + ' |')


    @staticmethod
    # Providing the number that corresponds to each cell
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print ('| ' +  ' | '.join(row) + ' |')


    def available_moves(self):
        # Returning a list of the current empty cells
        return [i for i, spot in enumerate(self.board) if spot == ' ']


    def empty_squares(self):
        # Checking if a cell is empty
        return ' ' in self.board
    

    def num_empty_squares(self):
        # Returning the number of the empty cells
        return self.board.count(' ')
        

    def make_move(self, square, letter):
        # If the move is valid, then make the move (assign the letter to the chosen cell) and return True
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        # If the move is not valid return False
        else:
            return False


    def winner(self, square, letter):
        # Checking if there are three of the same letter in a row 
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Checking if there are three of the same letter in a column
        col_ind = square % 3
        column = [self. board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True 

        # Checking if there are three of the same letter in a diagonal
        if square % 2 == 0:
            # Left to right diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            #Right to left diagonal 
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True  
        else:
            return False      


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    # Starting letter
    letter = 'X'

    while game.empty_squares():
        # Getting the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

                # Returns the winner of the game if its not a tie
                if game.current_winner:
                    if print_game:
                        print(letter + " <- WINS !!")
                    return letter
                
                letter = 'O' if letter == 'X' else 'X'
        time.sleep(0.8)

    if print_game:
        print("Its a TIE !!")   