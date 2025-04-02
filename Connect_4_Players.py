import math
from Connect_4_Board import Board

class Player:

    def __init__(self, depthLimit, isPlayerOne):
        # Initializing the player with a depth limit 
        self.isPlayerOne = isPlayerOne
        self.depthLimit = depthLimit

    def heuristic(self, board):
        # Evaluating the heuristic value of the current state of the board.
        heur = 0
        state = board.board

        for i in range(0, board.WIDTH):
            for j in range(0, board.HEIGHT):
                # Checking for horizontal connections.
                try:
                    # Checking for a sequence of three consecutive 0s (Player One's piece)
                    if state[i][j] == state[i + 1][j] == 0:
                        heur += 10
                    # Checking for a sequence of three consecutive 0s
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == 0:
                        heur += 100
                    # Checking for a sequence of four consecutive 0s
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == 0:
                        heur += 10000

                    # Checking for a sequence of two consecutive 1s (Player Two's piece)
                    if state[i][j] == state[i + 1][j] == 1:
                        heur -= 10
                    # Checking for a sequence of three consecutive 1s
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == 1:
                        heur -= 100
                    # Checking for a sequence of four consecutive 1s
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == 1:
                        heur -= 10000
                except IndexError:
                    pass

                # Checking for vertical connections.
                try:
                    # Checking for a sequence of three consecutive 0s (Player One's piece)
                    if state[i][j] == state[i][j + 1] == 0:
                        heur += 10
                    # Checking for a sequence of three consecutive 0s
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == 0:
                        heur += 100
                    # Checking for a sequence of four consecutive 0s
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == 0:
                        heur += 10000

                    # Checking for a sequence of two consecutive 1s (Player Two's piece)
                    if state[i][j] == state[i][j + 1] == 1:
                        heur -= 10
                    # Checking for a sequence of three consecutive 1s
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == 1:
                        heur -= 100
                    # Checking for a sequence of four consecutive 1s
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == 1:
                        heur -= 10000
                except IndexError:
                    pass

                # Check for diagonal connections (top-left to bottom-right).
                try:
                    # Checking for a sequence of three consecutive 0s (Player One's piece)
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == 0:
                        heur += 100
                    # Checking for a sequence of three consecutive 0s
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == 0:
                        heur += 100
                    # Checking for a sequence of four consecutive 0s
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] \
                            == state[i+3][j + 3] == 0:
                        heur += 10000

                    # Checking for a sequence of two consecutive 1s (Player Two's piece)
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == 1:
                        heur -= 100
                    # Checking for a sequence of three consecutive 1s
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == 1:
                        heur -= 100
                     # Checking for a sequence of four consecutive 1s
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] \
                            == state[i+3][j + 3] == 1:
                        heur -= 10000
                except IndexError:
                    pass

                # Check for diagonal connections (top-right to bottom-left).
                try:
                    # Checking for a sequence of three consecutive 0s (Player One's piece)
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == 0:
                        heur += 10
                    # Checking for a sequence of three consecutive 0s
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == 0:
                        heur += 100
                    # Checking for a sequence of four consecutive 0s
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] \
                            == state[i+3][j - 3] == 0:
                        heur += 10000

                    # Checking for a sequence of two consecutive 1s (Player Two's piece)
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == 1:
                        heur -= 10
                    # Checking for a sequence of three consecutive 1s
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == 1:
                        heur -= 100
                    # Checking for a sequence of four consecutive 1s
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] \
                            == state[i+3][j - 3] == 1:
                        heur -= 10000
                except IndexError:
                    pass
        return heur


class PlayerMM(Player):
    def __init__(self, depthLimit, isPlayerOne):
        # Initializing the PlayerMin-Max class by calling the constructor of the base class (Player).
        super().__init__(depthLimit, isPlayerOne)

    def findMove(self, board):
        # Finding the best move using the min-max algorithm and print the move made.
        score, move = self.miniMax(board, self.depthLimit, self.isPlayerOne)
        print(self.isPlayerOne, "move made", move)
        return move

    def miniMax(self, board, depth, player):
        # Implementation of the min-max algorithm for finding the best move.

        # Base case: Checking if the game has reached a terminal state.
        if board.isTerminal() == 0:
            return -math.inf if player else math.inf, -1
        # Base case: Checking if the maximum depth is reached.
        elif depth == 0:
            return self.heuristic(board), -1

        # Initializeing the best score and move based on the current player.
        if player:
            bestScore = -math.inf
            shouldReplace = lambda x: x > bestScore
        else:
            bestScore = math.inf
            shouldReplace = lambda x: x < bestScore

        bestMove = -1

        # Generating children (possible moves) for the current board.
        children = board.children()
        for child in children:
            move, childboard = child
            # Recursively calling min_max on the child board to get its score.
            temp = self.miniMax(childboard, depth - 1, not player)[0]
            # Updating the best score and move if the current move is better.
            if shouldReplace(temp):
                bestScore = temp
                bestMove = move
        return bestScore, bestMove

    def mmH(self, board, depth, player):
        # Heuristic function for the minimax algorithm.

        # Base case: Checking if the maximum depth is reached.
        if depth == 0:
            # Generating children (possible moves) for the current board.
            boards = board.children()
            scores = {}
            # Calculating heuristic scores for each child board.
            for i in boards:
                scores[i[0]] = self.heuristic(i[1])
            # Returning the move with the maximum or minimum heuristic score based on the player.
            if player:
                return max(scores, key=lambda k: scores[k])
            else:
                return min(scores, key=lambda k: scores[k])
        else:
            # Recursively calling mmH to explore deeper levels of the game tree.
            return self.mmH(board, depth - 1, not player)

class PlayerAB(Player):

    def __init__(self, depthLimit, isPlayerOne):
        # Initializing the PlayerAlpha-Beta class by calling the constructor of the base class (Player).
        super().__init__(depthLimit, isPlayerOne)

    def findMove(self, board):
        # Calling the alpha-beta pruning function to find the best move
        score, move = self.alphaBeta(board, self.depthLimit, self.isPlayerOne, -math.inf, math.inf)
        return move

    def alphaBeta(self, board, depth, player, alpha, beta):
        # Checking if the current board state is a terminal state
        if board.isTerminal() == 0:
            # Returning negative infinity for player one and positive infinity for player two
            return -math.inf if player else math.inf, -1
        # Checking if the maximum depth is reached
        elif depth == 0:
            # Return the heuristic value for the current board state
            return self.heuristic(board), -1

        # Initializing the best score and move
        if player:
            bestScore = -math.inf
            shouldReplace = lambda x: x > bestScore
        else:
            bestScore = math.inf
            shouldReplace = lambda x: x < bestScore

        bestMove = -1

        # Generating possible child moves from the current board state
        children = board.children()
        for child in children:
            move, childboard = child
            # Recursively calling alpha-beta on child nodes
            temp = self.alphaBeta(childboard, depth-1, not player, alpha, beta)[0]
            # Updating the best score and move if needed
            if shouldReplace(temp):
                bestScore = temp
                bestMove = move
            # Updating alpha and beta based on the current player
            if player:
                alpha = max(alpha, temp)
            else:
                beta = min(beta, temp)
            # Performing alpha-beta pruning
            if alpha >= beta:
                break
        return bestScore, bestMove


class Game:

    def __init__(self, startBoard, player1, player2):
        # Initializing the game with the starting board and two players
        self.startBoard = startBoard
        self.player1 = player1
        self.player2 = player2

    def simulateLocalGame(self):
        # Creating a copy of the starting board for simulation
        board = Board(orig=self.startBoard)
        # Initializing the current player as Player 1
        isPlayer1 = True

        # Continuing the game until it reaches a terminal state
        while True:
            # Determining the move for the current player
            if isPlayer1:
                move = self.player1.findMove(board)
            else:
                move = self.player2.findMove(board)

            # Making the selected move on the board
            board.makeMove(move)
            # Printing the current state of the board
            board.print()

            # Checking if the game is over
            isOver = board.isTerminal()
            if isOver == 0:
                print("It is a draw!")
                break
            elif isOver == 1:
                print("Player 1 wins!")
                break
            elif isOver == 2:
                print("Player 2 wins!")
                break
            else:
                # Switching to the other player for the next turn
                isPlayer1 = not isPlayer1