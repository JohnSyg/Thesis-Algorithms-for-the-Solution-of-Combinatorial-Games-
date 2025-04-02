from Eight_Puzzle_Node import *

class Searcher(object):
    # Initializing the Searcher object with a start state and a goal state
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal


    # Printing the path from the start state to the given state
    def print_path(self, state):
        path = []
        while state:
            path.append(state)
            state = state.prev
        path.reverse()
        print("\n_____\n".join([str(state) for state in path]))


    # Performing a breadth-first search to find a solution
    def bfs(self, depth = 50):
        # Reseting the expanded nodes counter
        Node.n=0
        # Initializing the queue with the start state
        queue = [self.start]
        # Creating a set to keep track of visited states
        visited = set()
        # Initializing a variable to track whether a solution has been found
        found = False

        # Continuing searching until the queue is empty or a solution is found
        while queue:
            # Removing and returning the first state from the queue
            state = queue.pop()

            # Checking if the current state is the goal state
            if state == self.goal:
                found = state
                break

            # Checking if the current state has been visited before or exceeds the depth limit
            if state in visited or state.step > depth:
                continue

            # Marking the current state as visited
            visited.add(state)

            # Generating the next states from the current state and adding them to the front of the queue
            for s in state.next():
                queue.insert(0, s)

        # Checking if a solution was found
        if found:
            # Printing the path to the solution
            self.print_path(found)
            print ("Solution found")
        else:
            print("No solution found")


    # Performing a depth-first search to find a solution
    def dfs(self, depth = 100):
        # Reseting the expanded nodes counter
        Node.n=0
        # Initializing the stack with the start state
        stack = [self.start]
        # Creating a set to keep track of visited states
        visited = set()
        # Initializing a variable to track whether a solution has been found
        found = False

        # Continuing searching until the queue is empty or a solution is found
        while stack:
            # Removing and returning the first state from the stack
            state = stack.pop()

            # Checking if the current state is the goal state
            if state == self.goal:
                found = state
                break

            # Checking if the current state has been visited before or exceeds the depth limit
            if state in visited or state.step > depth:
                continue

            # Marking the current state as visited
            visited.add(state)

            # Generating the next states from the current state and adding them to the top of the stack
            for s in state.next():
                stack.append(s)

        # Checking if a solution was found
        if found:
            # Printing the path to the solution
            self.print_path(found)
            print ("Find solution")
        else:
            print("No solution found")


    # Perform an A* search with Manhattan distance heuristic to find a solution   
    def astar_md(self, depth = 75):
        # Reseting the expanded nodes counter
        Node.n=0
        # Creating a priority queue to store states based on their f-value
        priotity_queue = PriorityQueue()

        # Calculating the Manhattan distance heuristic for the start state
        h_val = self.start.manhattan_distance()
        # Calculating the f-value for the start state 
        f_val = h_val + self.start.step

        # Pushing the start state into the priority queue with its f-value as the priority
        priotity_queue.push(self.start, f_val)
        # Creating a set to keep track of visited states
        visited = set()
        # Initializing a variable to track whether a solution has been found
        found = False

        # Continuing searching until the priority queue is empty or a solution is found
        while not priotity_queue.isEmpty():
            # Popping the state with the lowest f-value from the priority queue
            state = priotity_queue.pop()

            # Checking if the current state is the goal state
            if state == self.goal:
                found = state
                break

            # Checking if the current state has been visited before or exceeds the depth limit
            if state in visited or state.step > depth:
                continue

            # Marking the current state as visited
            visited.add(state)

            # Generating the next states from the current state
            for s in state.next():
                # Calculating the Manhattan distance heuristic for the next state
                h_val_s = s.manhattan_distance()
                # Calculatint the f-value for the next state
                f_val_s = h_val_s + s.step
                # Pushing the next state into the priority queue with its f-value as the priority
                priotity_queue.push(s, f_val_s)

        # Checking if a solution was found
        if found:
            # Printing the path to the solution
            self.print_path(found)
            print ("Solution found")
        else:
            print("No solution found")


    # Performing an A* search with Manhattan distance heuristic and reversal penalty to find a solution
    def astar_mdrp(self, depth = 75):
        # Reseting the expanded nodes counter
        Node.n=0
        # Creating a priority queue to store states based on their f-value
        priotity_queue = PriorityQueue()

        # Calculating the Manhattan distance plus reversal penalty heuristic for the start state
        h_val = self.start.manhattan_distance_plus_reversal_penalty()
        # Calculating the f-value for the start state 
        f_val = h_val + self.start.step

        # Pushing the start state into the priority queue with its f-value as the priority
        priotity_queue.push(self.start, f_val)
        # Creating a set to keep track of visited states
        visited = set()
        # Initializing a variable to track whether a solution has been found
        found = False

        # Continuing searching until the priority queue is empty or a solution is found
        while not priotity_queue.isEmpty():
            # Popping the state with the lowest f-value from the priority queue
            state = priotity_queue.pop()

            # Checking if the current state is the goal state
            if state == self.goal:
                found = state
                break

            # Checking if the current state has been visited before or exceeds the depth limit
            if state in visited or state.step > depth:
                continue

            # Marking the current state as visited
            visited.add(state)

            # Generating the next states from the current state
            for s in state.next():
                # Calculating the Manhattan distance plus reversal penalty heuristic for the next state
                h_val_s = s.manhattan_distance_plus_reversal_penalty()
                # Calculating the f-value for the next state
                f_val_s = h_val_s + s.step
                # Pushing the next state into the priority queue with its f-value as the priority
                priotity_queue.push(s, f_val_s)

        # Checking if a solution was found
        if found:
            # Printing the path to the solution
            self.print_path(found)
            print ("Solution found")
        else:
            print("No solution found")


    # Performing a Branch and Bound search to find a solution
    def b_and_b(self, depth = 75):
        # Reseting the expanded nodes counter
        Node.n=0
        # Creating a priority queue to store states based on their f-value
        priotity_queue = PriorityQueue()

        # Calculating the misplaced tiles heuristic for the start state
        h_val = self.start.misplaced_tiles() 
        # Calculating the f-value for the start state
        f_val = h_val + self.start.step

        # Pushing the start state into the priority queue with its f-value as the priority
        priotity_queue.push(self.start, f_val)
        # Creating a set to keep track of visited states
        visited = set()
        # Initializing a variable to track whether a solution has been found
        found = False

        # Continuing searching until the priority queue is empty or a solution is found
        while not priotity_queue.isEmpty():
            # Popping the state with the lowest f-value from the priority queue
            state = priotity_queue.pop()

            # Checking if the current state is the goal state
            if state == self.goal:
                found = state
                break

            # Checking if the current state has been visited before or exceeds the depth limit
            if state in visited or state.step > depth:
                continue

            # Marking the current state as visited
            visited.add(state)

            # Generating the next states from the current state
            for s in state.next():
                # Calculating the misplaced tiles heuristic for the next state
                h_val_s = s.misplaced_tiles()
                # Calculating the f-value for the next state
                f_val_s = h_val_s + s.step
                # Pushing the next state into the priority queue with its f-value as the priority
                priotity_queue.push(s, f_val_s)

        # Checking if a solution was found
        if found:
            # Printing the path to the solution
            self.print_path(found)
            print ("Solution found")
        else:
            print("No solution found")

    
    # Performing an Iterative Deepening Depth-First Search to find a solution
    def ids(self, depth = 0):
        # Reseting the expanded nodes counter
        Node.n=0
        # Creating a queue to store states
        queue = [self.start]
        # Creating a set to keep track of visited states
        visited = set()
        # Initializing a variable to track whether a solution has been found
        found = False

        # Continuing searching until the queue is empty or a solution is found
        while queue:
            # Removing and returning the first state from the queue
            state = queue.pop()

            # Checking if the current state is the goal state
            if state == self.goal:
                found = state
                break

            # Checking if the current state has been visited before or exceeds the depth limit
            if state in visited or state.step > depth:
            # Increasing the depth limit
                depth += 1
                continue

            # Marking the current state as visited
            visited.add(state)

            # Generating the next states from the current state
            for s in state.next():
                # Inserting the next state at the front of the queue
                queue.insert(0, s)

        # Checking if a solution was found
        if found:
            # Printing the path to the solution
            self.print_path(found)
            print ("Solution found")
            print("Depth: " , depth)
        else:
            print("No solution found")