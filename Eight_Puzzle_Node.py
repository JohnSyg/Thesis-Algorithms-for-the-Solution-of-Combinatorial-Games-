import heapq

# Node class representing a state of the puzzle 
class Node(object):
    n = 0

    def __init__(self, board, prev_state = None):
        assert len(board) == 9

        # Copy the board state
        self.board = board[:]
        # Previous state (Parent)
        self.prev = prev_state
        # Number of steps taken from the initial state to this state
        self.step = 0
        Node.n += 1

        # Calculate the step count from the previous state
        if self.prev:
            self.step = self.prev.step + 1 

    def __eq__(self, other):
        return self.board == other.board

    # Calculate hash values for each row of the board
    def __hash__(self):
        h = [0, 0, 0]
        h[0] = self.board[0] << 6 | self.board[1] << 3 | self.board[2]
        h[1] = self.board[3] << 6 | self.board[4] << 3 | self.board[5]
        h[2] = self.board[6] << 6 | self.board[7] << 3 | self.board[8]

        # Combine the hash values using a weighted sum
        h_val = 0
        for h_i in h:
            h_val = h_val * 31 + h_i

        return h_val

    # Creating the string representation of the board
    def __str__(self):
        string_list = [str(i) for i in self.board]
        sub_list = (string_list[:3], string_list[3:6], string_list[6:])
        return "\n".join([" ".join(l) for l in sub_list])
    
  
  
    # Convert the given index to a position on a 2D board
    def __i2pos(self, index):
        # Dividing the index by 3 to get the row number and taking the remainder when divided by 3 to get the column number
        return (int(index / 3), index % 3)

    # Convert the given row and column numbers to an index on a 1D board
    def __pos2i(self, x, y):
        # Multiplying the row number by 3 and adding the column number
        return x * 3 + y
    
    # Checking how many tiles are misplaced
    def misplaced_tiles(self):
        count = 0
        goal = [1,2,3,4,5,6,7,8,0]
        for i in range(1,9):
            xs, ys = self.__i2pos(self.board.index(i))
            xg, yg = self.__i2pos(goal.index(i))
            # Check if the current position and the goal position differ in both the row and column
            if xs != xg and ys != yg:
                # If they differ, increment the count since the number i is in the wrong position
                count += 1
        return count

    # Calculating the manhattan distance
    def manhattan_distance(self):
        distance = 0
        goal = [1,2,3,4,5,6,7,8,0]
        for i in range(1,9):
            xs, ys = self.__i2pos(self.board.index(i))
            xg, yg = self.__i2pos(goal.index(i))
            # Manhattan distance between the current position and the goal position
            distance += abs(xs-xg) + abs(ys-yg)
        return distance
    
    # Choosing direction depending on the current position and the goal position
    def get_direction(self, xs, ys, xg, yg):
        if xs == xg:
            if ys < yg:
                return 'Right'
            else:
                return 'Left'
        elif ys == yg:
            if xs < xg:
                return 'Down'
            else:
                return 'Up'
        else:
            return ''

    # Calculate the manhattan distance but also add a penalty for every change of direction 
    def manhattan_distance_plus_reversal_penalty(self):
        distance = 0
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        current_direction = ''
        num_direction_changes = 0
        for i in range(1, 9):
            xs, ys = self.__i2pos(self.board.index(i))
            xg, yg = self.__i2pos(goal.index(i))
            distance += abs(xs - xg) + abs(ys - yg)
            # Checking if there is a current direction and compare it with the new direction
            if current_direction != '':
                if current_direction != self.get_direction(xs, ys, xg, yg):
                    # If the direction has changed, increment the number of direction changes
                    num_direction_changes += 1
            current_direction = self.get_direction(xs, ys, xg, yg)
        return distance + num_direction_changes

    # Generate the possible next moves
    def next(self):
        next_moves = []
        i = self.board.index(0)

        # Calling the move methods for each direction
        next_moves = (self.move_up(i), self.move_down(i), self.move_left(i), self.move_right(i))

        # Return a filtered list that contains only valid moves
        return [s for s in next_moves if s]
    
    # Swaping places between two tiles
    def __swap(self, i, j):
        self.board[j], self.board[i] = self.board[i], self.board[j]

    # Creating the new state after a right move
    def move_right(self, i):
        x, y = self.__i2pos(i)
        if y < 2:
            right_state = Node(self.board, self)
            right = self.__pos2i(x, y + 1)
            right_state.__swap(i, right)
            return right_state

    # Creating the new state after a left move
    def move_left(self, i):
        x, y = self.__i2pos(i)
        if y > 0:
            left_state = Node(self.board, self)
            left = self.__pos2i(x, y - 1)
            left_state.__swap(i, left)
            return left_state
        
    # Creating the new state after an upwards move
    def move_up(self, i):
        x, y = self.__i2pos(i)
        if x > 0:
            up_state = Node(self.board, self)
            up = self.__pos2i(x - 1, y)
            up_state.__swap(i, up)
            return up_state

    # Creating the new state after a downwards move
    def move_down(self, i):
        x, y = self.__i2pos(i)
        if x < 2:
            down_state = Node(self.board, self)
            down = self.__pos2i(x + 1, y)
            down_state.__swap(i, down)
            return down_state

# PriorityQueue class for efficient priority-based sorting  
class PriorityQueue:
    # Initialize an empty list to serve as the heap and a counter to keep track of the insertion order
    def  __init__(self):
        self.heap = []
        self.count = 0

    # Push the entry onto the heap
    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    # Pop the entry with the lowest priority (based on the heap order)
    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    # Check if the heap is empty by comparing its length to 0
    def isEmpty(self):
        return len(self.heap) == 0