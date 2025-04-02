import heapq
import sys
from collections import deque
from The_Knight_Problem_Node import *

# Printing the path from start to goal
def printPath(node):
    path = []
    while node:
        path.append((node.x, node.y))
        node = node.parent
    path.reverse()
    print("Path:")
    for position in path:
        print(position)


# Performing a breadth-first search to find the shortest path
def bfs(start, goal, N):
    # Reseting the expanded nodes counter
    Knight_Node.n=0
    # Creating an empty deque (double-ended queue)
    queue = deque()
    # Adding the statring node to the queue
    queue.append(start)
    # Creating a set to keep track of visited states
    visited = set()
    # Initializing a variable to track whether a solution has been found
    found = False
 
    # Continuing searching until the queue is empty or a solution is found
    while queue:
        # Removing the node from the left end of the queue
        state = queue.popleft()
 
        # Assigning the pawn's attributes in a state
        x = state.x
        y = state.y
        moves = state.moves
 
        # Checking if the current state is the goal state
        if x == goal.x and y == goal.y:
            found = state
            break
 
        # Checking if the current state has been visited before
        if state in visited:
            continue

        # Marking the current state as visited
        visited.add(state)
 
        # Generating the next states from the current state and adding them to the front of the queue
        for i in range(8):
            
            x1 = x + row[i]
            y1 = y + col[i]
 
            if isValid(x1, y1, N):
                queue.append(Knight_Node(x1, y1, moves + 1, parent=state))

    # Checking if a solution was found        
    if found:
        # Printing the moves needed to reach the goal and the path to it
        print ('Solution found\nMoves needed:', moves)
        printPath(state)  
    else:
        print('No solution found')


# Performing a depth-first search to find the shortest path
def dfs(start, goal, N):
    # Reseting the expanded nodes counter
    Knight_Node.n = 0
    # Creating an empty stack
    stack = []
    # Adding the statring node to the the top of the stack
    stack.insert(0,start)
    # Creating a set to keep track of visited states
    visited = set()
    # Initializing a variable to track whether a solution has been found
    found = False

    # Continuing searching until the stack is empty or a solution is found
    while stack:
        # Removing the first state from the stack
        state = stack.pop()

        # Assigning the pawn's attributes in a state
        x = state.x
        y = state.y
        moves = state.moves

        # Checking if the current state is the goal state
        if x == goal.x and y == goal.y:
            found = state
            break

        # Checking if the current state has been visited before
        if state in visited:
            continue

        # Marking the current state as visited
        visited.add(state)

        # Generating the next states from the current state and adding them to the top of the stack
        for i in range(8):
            x1 = x + row[i]
            y1 = y + col[i]

            if isValid(x1, y1, N):
                stack.insert(0,Knight_Node(x1, y1, moves + 1,parent=state))  

    # Checking if a solution was found    
    if found:
        # Printing the moves needed to reach the goal and the path to it
        print('Solution found\nSteps needed:', moves)  
        printPath(state)
    else:
        print('No solution found')


# Performimg an A* search with Manhattan distance heuristic to find the shortest path
def astar_md(start, goal, N):
    # Reseting the expanded nodes counter
    Knight_Node.n = 0
    # Creating an empty queue
    queue = []
    # Calculating the mahattan distance for the starting possition of the pawn
    start.h = manhattan_distance(start.x, start.y, goal.x, goal.y)
    # Adding the statring node to the queue using a heap-based priority
    heapq.heappush(queue, start)
    # Creating a set to keep track of visited states
    visited = set()
    # Initializing a variable to track whether a solution has been found
    found = False

    # Continuing searching until the queue is empty or a solution is found
    while queue:
        # Removing a node, based on its priority, from the queue
        state = heapq.heappop(queue)

        # Assigning the pawn's attributes in a state
        x = state.x
        y = state.y
        moves = state.moves

        # Checking if the current state is the goal state
        if x == goal.x and y == goal.y:
            found = state
            break

        # Checking if the current state has been visited before
        if state in visited:
            continue

        # Marking the current state as visited
        visited.add(state)

        # Generating the next states from the current state and adding them to the queue (the priority is provided by the manhattan distance calculated of each move)
        for i in range(8):
            x1 = x + row[i]
            y1 = y + col[i]

            if isValid(x1, y1, N):
                node = Knight_Node(x1, y1, moves + 1, parent=state)
                node.h = manhattan_distance(x1, y1, goal.x, goal.y)
                heapq.heappush(queue, node)

    # Checking if a solution was found 
    if found:
        # Printing the moves needed to reach the goal and the path to it
        print('Solution found\nSteps needed:', moves)
        printPath(state)
    else:
        print('No solution found')


# Performing an A* search with Manhattan distance heuristic and reversal penalty to find the shortest path
def astar_mdrp(start, goal, N):
    # Reseting the expanded nodes counter
    Knight_Node.n = 0
    # Creating an empty queue
    queue = []
    # Calculating the mahattan distance with reversal penalty for the starting possition of the pawn
    start.h = manhattan_distance_with_reversal_penalty(start.x, start.y, goal.x, goal.y,1)
    # Adding the statring node to the queue using a heap-based priority
    heapq.heappush(queue, start)
    # Creating a set to keep track of visited states
    visited = set()
    # Initializing a variable to track whether a solution has been found
    found = False

    # Continuing searching until the queue is empty or a solution is found
    while queue:
        # Removing a node, based on its priority, from the queue
        state = heapq.heappop(queue)

        # Assigning the pawn's attributes in a state
        x = state.x
        y = state.y
        moves = state.moves

        # Checking if the current state is the goal state
        if x == goal.x and y == goal.y:
            found = state
            break

        # Checking if the current state has been visited before
        if state in visited:
            continue

        # Marking the current state as visited
        visited.add(state)

        # Generating the next states from the current state and adding them to the queue (the priority is provided by the manhattan distance with reversal penalty calculated of each move)
        for i in range(8):
            x1 = x + row[i]
            y1 = y + col[i]

            if isValid(x1, y1, N):
                node = Knight_Node(x1, y1, moves + 1, parent=state)
                node.h = manhattan_distance_with_reversal_penalty(x1, y1, goal.x, goal.y,1)
                heapq.heappush(queue, node)

    # Checking if a solution was found 
    if found:
        # Printing the moves needed to reach the goal and the path to it
        print('Solution found\nSteps needed:', moves)
        printPath(state)
    else:
        print('No solution found')


# Performing a Branch and Bound search to find the shortest path
def b_and_b(start, goal, N):
    # Reseting the expanded nodes counter
    Knight_Node.n = 0
    # Creating an empty queue
    queue = []
    # Calculating the mahattan distance for the starting possition of the pawn
    start.h = manhattan_distance(start.x, start.y, goal.x, goal.y)
    # Adding the statring node to the queue using a heap-based priority
    heapq.heappush(queue, start)
    # Creating a set to keep track of visited states
    visited = set()
    # Initializing a variable to track whether a solution has been found
    found = False
    # Initializing the best lower bound estimate
    best_lb = float('inf')  

    # Continuing searching until the queue is empty or a solution is found
    while queue:
        # Removing a node, based on its priority, from the queue
        state = heapq.heappop(queue)

        # Assigning the pawn's attributes in a state
        x = state.x
        y = state.y
        moves = state.moves

        # Checking if the current state is the goal state
        if x == goal.x and y == goal.y:
            found = state
            break

        # Checking if the current state has been visited before
        if state in visited:
            continue

        # Marking the current state as visited
        visited.add(state)

        # Generating the next states from the current state and adding them to the queue (the priority is provided by the manhattan distance and the lower bound calculated of each move)
        for i in range(8):
            x1 = x + row[i]
            y1 = y + col[i]

            if isValid(x1, y1, N):
                node = Knight_Node(x1, y1, moves + 1, parent=state)
                node.h = manhattan_distance(x1, y1, goal.x, goal.y)
                if node.h < best_lb:
                    # Calculating the lower bound estimate
                    node.lb = moves + 1 + node.h  
                    heapq.heappush(queue, node)
                    best_lb = node.lb

    # Checking if a solution was found 
    if found:
        # Printing the moves needed to reach the goal and the path to it
        print('Solution found\nSteps needed:', moves)
        printPath(state)
    else:
        print('No solution found')


# Performing an Iterative Deepening Depth-First Search to find the shortest path
def ids(start, goal, N, depth):
    # Reseting the expanded nodes counter
    Knight_Node.n=0
    # Creating an empty deque (double-ended queue)
    q = deque()
    # Adding the statring node to the queue
    q.append(start)
    # Creating a set to keep track of visited states
    visited = set()
    # Initializing a variable to track whether a solution has been found
    found = False
 
    # Continuing searching until the queue is empty or a solution is found
    while q:
        # Removing the node from the left end of the queue
        state = q.popleft()
 
        # Assigning the pawn's attributes in a state
        x = state.x
        y = state.y
        moves = state.moves
 
        # Checking if the current state is the goal state
        if x == goal.x and y == goal.y:
            found = state
            break
 
        # Checking if the current state has been visited before or exceeds the depth limit
        if state in visited or moves > depth:
            depth += 1
            continue

        # Marking the current state as visited
        visited.add(state)
 
        # Generating the next states from the current state and adding them to the front of the queue
        for i in range(8):
            x1 = x + row[i]
            y1 = y + col[i]
 
            if isValid(x1, y1, N):
                q.append(Knight_Node(x1, y1, moves + 1, parent=state))

    # Checking if a solution was found       
    if found:
        # Printing the moves needed to reach the goal and the path to it
        print ('Solution found\nSteps needed:', moves)
        printPath(state)
    else:
        print('No solution found')