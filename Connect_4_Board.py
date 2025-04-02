import random

class Board(object):

    # Defining constants for the board dimensions
    HEIGHT = 6
    WIDTH = 7

    # Constructor for the Board class
    def __init__(self, orig=None, hash=None, randomize=False):

        # If 'orig' is provided, creating a copy of the board
        if(orig):
            self.board = [list(col) for col in orig.board]
            self.numMoves = orig.numMoves
            self.lastMove = orig.lastMove
            return

        # If 'hash' is provided, reconstructing the board from the hash value
        elif(hash):
            self.board = []
            self.numMoves = 0
            self.lastMove = None

            digits = []
            # Converting hash to base-3 digits
            while hash:
                digits.append(int(hash % 3))
                hash //= 3

            col = []
            
            # Reconstructing the board from base-3 digits
            for item in digits:
                if item == 2:
                    self.board.append(col)
                    col = []
                else:
                    col.append(item)
                    self.numMoves += 1
            return

        # If neither 'orig' nor 'hash' is provided, initializing an empty board
        else:
            self.board = [[] for x in range(self.WIDTH)]
            self.numMoves = 0
            self.lastMove = None
            
            # If randomize is True, shuffling the initial board state
            if randomize:
                self.randomizeBoard()

    # Making a move on the board
    def makeMove(self, column):
        # Updating board data
        piece = self.numMoves % 2
        self.lastMove = (piece, column)
        self.numMoves += 1
        self.board[column].append(piece)

    # Generating possible child boards for the current board state
    def children(self):
        children = []
        for i in range(7):
            if len(self.board[i]) < 6:
                child = Board(self)
                child.makeMove(i)
                children.append((i, child))
        return children

    # Checking if the game has reached a terminal state
    def isTerminal(self):
        for i in range(0,self.WIDTH):
            for j in range(0,self.HEIGHT):
                try:
                    # Checking for a horizontal win
                    if self.board[i][j]  == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    # Checking for a vertical win
                    if self.board[i][j]  == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    # Checking for a diagonal win (bottom-left to top-right)
                    if not j + 3 > self.HEIGHT and self.board[i][j] == self.board[i+1][j + 1] == self.board[i+2][j + 2] == self.board[i+3][j + 3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    # Checking for a diagonal win (top-left to bottom-right)
                    if not j - 3 < 0 and self.board[i][j] == self.board[i+1][j - 1] == self.board[i+2][j - 2] == self.board[i+3][j - 3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass
        # If the board is full, returning a draw
        if self.isFull():
            return 0
        # If the game is not over, returning -1
        return -1

    # Generating a hash value for the current board state
    def hash(self):

        power = 0
        hash = 0

        # Converting the board state to a hash value using base-3 encoding
        for column in self.board:
            for piece in column:
                hash += piece * (3 ** power)
                power += 1

            hash += 2 * (3 ** power)
            power += 1

        return hash
    
    # Checking if the board is full
    def isFull(self):
        return self.numMoves == 42

    # Printing the current board state
    def print(self):
        print("")
        print("+" + "---+" * self.WIDTH)
        for rowNum in range(self.HEIGHT - 1, -1, -1):
            row = "|"
            for colNum in range(self.WIDTH):
                if len(self.board[colNum]) > rowNum:
                    row += " " + ('X' if self.board[colNum][rowNum] else 'O') + " |"
                else:
                    row += "   |"
            print(row)
            print("+" + "---+" * self.WIDTH)
        print(self.lastMove[1])
        print(self.numMoves)