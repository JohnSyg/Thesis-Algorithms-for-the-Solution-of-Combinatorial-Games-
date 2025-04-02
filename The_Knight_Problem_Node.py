# Node class representing a state of the pawn
class Knight_Node:
    n = 0
    
    def __init__(self, x, y, moves=0, parent=None):
        # X coordinate of the Knight pawn
        self.x = x
        # Y coordinate of the Knight pawn
        self.y = y
        # Number of moves taken by the pawn
        self.moves = moves
        # Previous state of the pawn (Parent)
        self.parent = parent
        Knight_Node.n += 1
 
    # Using `Node` as a key in a dictionary
    # Overriding the hash function for `Knight_Node` objects
    def __hash__(self):
        return hash((self.x, self.y, self.moves))
    
    # Overriding the equality comparison for `Knight_Node` objects
    def __eq__(self, other):
        return (self.x, self.y, self.moves) == (other.x, other.y, other.moves)
 
    # Overriding the less than comparison for `Knight_Node` objects
    def __lt__(self, other):
        return self.moves + self.h < other.moves + other.h
 
# Providing all eight possible movements for the knight pawn
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]
 
# Checking if the provided (x, y) coordinates are within the limits of the chessboard
def isValid(x, y, N):
    return not (x < 0 or y < 0 or x >= N or y >= N)

# Calculating the manhattan distance of the pawn 
def manhattan_distance(x, y, dest_x, dest_y):
    return abs(dest_x - x) + abs(dest_y - y)

# Calculating the manhattan distance and adding a reversal penalty on certain directions
def manhattan_distance_with_reversal_penalty(x, y, dest_x, dest_y, penalty):
    dx = abs(dest_x - x)
    dy = abs(dest_y - y)

    # Knight's valid moves
    if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):  
        return dx + dy
    # Reversal penalty
    elif dx * dy == 0 or dx == dy:  
        return dx + dy + penalty
    else:
        return dx + dy