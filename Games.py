from Tic_Tac_Toe_Algorithm import *
from Eight_Puzzle_Algorithms import *
from The_Knight_Problem_Algorithms import *
from Connect_4_Board import *
from Connect_4_Players import *
from time import time
import random

# Counting how many inversion the staring node has
def count_inversions(numbers):
    inversions = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j] and numbers[i] != 0 and numbers[j] != 0:
                inversions += 1
    return inversions

# Making the number of inversions an even number in case it is not (Cause the 8-Puzzle is not solvable otherwise)
def generate_even_inversions():
    numbers = list(range(9))
    random.shuffle(numbers)

    inversions = count_inversions(numbers)

    # Swap two elements to make the number of inversions even
    if inversions % 2 != 0:
        # Find two random indices to swap
        i, j = random.sample(range(len(numbers)), 2)
        
        # Swap the two elements
        numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

if __name__ == '__main__':

    # Initializing some colors for making it easier to read information on the terminal
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    MAGENTA = '\033[35m'
    RESET = '\033[0m'
    
    # Initializing a list that will keep track of 8-Puzzle information 
    results = []

    while(True):
        # Providing the user with the available games
        answer = input('\nChoose between one of the following options:\n1. Tic-Tac-Toe\n2. Connect-4\n3. 8-Puzzle\n4. The Knight Problem\n5. Exit\nAnswer: ')
    

        # Choosing Tic-Tac-Toe
        if answer == '1' or answer == 'Tic-Tac-Toe':
            while(True):
                # Providing the user with the options of Tic-Tac-Toe
                answer = input('\nChoose between one of the two opponents :\n1. Beginner\n2. Expert\nAnswer: ')
                if answer == '1' or answer == 'Beginner':
                    # Creating the two players 
                    x_player = HumanPlayer('X')
                    o_player = RandomComputerPlayer('O')
                    
                    print('\n')
                    # Enabling the game
                    t = TicTacToe()
                    play(t, x_player, o_player, print_game=True)
                    
                    # Checking if the user wants to continue playing 
                    answer = input('\nWould you like to continue playing the same game ??\n(YES/yes , NO/no)\nAnswer: ')
                    if answer == 'Yes' or answer == 'yes':
                        continue
                    else:
                        print('\nThanks for playing !!')
                        break
                elif answer == '2' or answer == 'Expert':
                    # Creating the two players 
                    x_player = HumanPlayer('X')
                    o_player = MinMaxComputerPlayer('O')
                    
                    print('\n')
                    # Enabling the game
                    t = TicTacToe()
                    play(t, x_player, o_player, print_game=True)
                    
                    # Checking if the user wants to continue playing 
                    answer = input('\nWould you like to continue playing the same game ??\n(YES/yes , NO/no)\nAnswer: ')
                    if answer == 'Yes' or answer == 'yes':
                        continue
                    else:
                        print('\nThanks for playing !!')
                        break
                else:
                    print('\nNot a valid opponent')
                
                
        # Choosing Connect-4
        elif answer == '2' or answer == 'Connect-4':
            while(True):
                # Choosing between the four available options
                answer = input('\nChoose between one of the available options :\n1. Alpa-Beta VS Alpha-Beta\n2. Min-Max VS Min-Max\n3. Min-Max VS Alpha-Beta\n4. Alpha-Beta VS Min-Max\nAnswer: ')
                # Alpa-Beta VS Alpha-Beta
                if answer == '1' or answer == 'Alpa-Beta VS Alpha-Beta':
                    depth = input('\nPlease choose the depth of search for the algorithms \nAnswer: ')
                    start_time = time()
                    game = Game(Board(), PlayerAB(int(depth), True), PlayerAB(int(depth), False))
                    game.simulateLocalGame()
                    end_time = time()
                    
                    # Keeping track of the run time
                    elapsed = end_time - start_time
                    print ('Search time: %s' % elapsed)

                    # Checking if the user wants to continue playing 
                    answer = input('\nWould you like to continue playing the same game ??\n(YES/yes , NO/no)\nAnswer: ')
                    if answer == 'Yes' or answer == 'yes':
                        continue
                    else:
                        print('\nThanks for playing !!')
                        break

                # Min-Max VS Min-Max
                elif answer == '2' or answer == 'Min-Max VS Min-Max':
                    depth = input('\nPlease choose the depth of search for the algorithms \nAnswer: ')
                    start_time = time()
                    game = Game(Board(), PlayerMM(int(depth), True), PlayerMM(int(depth), False))
                    game.simulateLocalGame()
                    end_time = time()

                    # Keeping track of the run time
                    elapsed = end_time - start_time
                    print ('Search time: %s' % elapsed)

                    # Checking if the user wants to continue playing 
                    answer = input('\nWould you like to continue playing the same game ??\n(YES/yes , NO/no)\nAnswer: ')
                    if answer == 'Yes' or answer == 'yes':
                        continue
                    else:
                        print('\nThanks for playing !!')
                        break

                # Min-Max VS Alpha-Beta
                elif answer == '3' or answer == 'Min-Max VS Alpha-Beta':
                    depth = input('\nPlease choose the depth of search for the algorithms \nAnswer: ')
                    start_time = time()
                    game = Game(Board(), PlayerMM(int(depth), True), PlayerAB(int(depth), False))
                    game.simulateLocalGame()
                    end_time = time()

                    # Keeping track of the run time
                    elapsed = end_time - start_time
                    print ('Search time: %s' % elapsed)

                    # Checking if the user wants to continue playing 
                    answer = input('\nWould you like to continue playing the same game ??\n(YES/yes , NO/no)\nAnswer: ')
                    if answer == 'Yes' or answer == 'yes':
                        continue
                    else:
                        print('\nThanks for playing !!')
                        break

                # Alpha-Beta VS Min-Max
                elif answer == '4' or answer == 'Alpha-Beta VS Min-Max':
                    depth = input('\nPlease choose the depth of search for the algorithms \nAnswer: ')
                    start_time = time()
                    game = Game(Board(), PlayerAB(int(depth), True), PlayerMM(int(depth), False))
                    game.simulateLocalGame()
                    end_time = time()

                    # Keeping track of the run time
                    elapsed = end_time - start_time
                    print ('Search time: %s' % elapsed)

                    # Checking if the user wants to continue playing 
                    answer = input('\nWould you like to continue playing the same game ??\n(YES/yes , NO/no)\nAnswer: ')
                    if answer == 'Yes' or answer == 'yes':
                        continue
                    else:
                        print('\nThanks for playing !!')
                        break
                else:
                    print('\nNot a valid option')
                
                
        # Choosing 8-Puzzle
        elif answer == '3' or answer == '8-Puzzle':
            while(True):
                print ('\nSolving the 8-Puzzle with the BFS, DFS, A*, B&B and IDS algorithms')

                # Initializing another list that will keep track of 8-Puzzle information
                run_results = []

                # Generating the random starting state
                numbers = generate_even_inversions()
                # Setting the starting state of the puzzle
                start = Node(numbers)
                # Setting the ending state of the puzzle
                goal = Node([1,2,3,4,5,6,7,8,0])

                search = Searcher(start, goal)


                # Solving the 8-Puzzle with BFS
                print ('\nBFS\n')
                start_time = time()
                search.bfs()
                end_time = time()

                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number of initialized node: %d' % Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "BFS", "Runtime": elapsed,"Expanded Nodes": Node.n})

                print ('\n----------------------------------------------------------')

                # Solving the 8-Puzzle with DFS
                print ('\nDFS\n')
                start_time = time()
                search.dfs()
                end_time = time()

                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number of initialized node: %d' % Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "DFS", "Runtime": elapsed,"Expanded Nodes": Node.n})

                print ('\n----------------------------------------------------------')


                # Solving the 8-Puzzle with A* utilizing the Manhattan Distance heuristic
                print ("\nA* (Manhattan Distance)\n")
                start_time = time()
                search.astar_md()
                end_time = time()

                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number node: %d' % Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "A* (Manhattan Distance)", "Runtime": elapsed,"Expanded Nodes": Node.n})

                print ("\n----------------------------------------------------------")


                # Solving the 8-Puzzle with A* utilizing the Manhattan Distance with Reversal Penalty search heuristic
                print ('\nA* (Manhattan Distance plus Reversal Penalty)\n')
                start_time = time()
                search.astar_mdrp()
                end_time = time()
                
                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number node: %d' % Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "A* (Manhattan Distance plus Reversal Penalty)", "Runtime": elapsed,"Expanded Nodes": Node.n})

                print ("\n----------------------------------------------------------")


                # Solving the 8-Puzzle with B&B
                print ('\nB&B\n')
                start_time = time()
                search.b_and_b()
                end_time = time()

                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number node: %d' % Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "B&B", "Runtime": elapsed,"Expanded Nodes": Node.n})

                print ('\n----------------------------------------------------------')


                # Solving the 8-Puzzle with IDS
                print ('\nIDS\n')
                start_time = time()
                search.ids()
                end_time = time()

                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number node: %d' % Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "IDS", "Runtime": elapsed,"Expanded Nodes": Node.n})

                # Inserting further information to the other list for the collective print
                results.append({"Start Configuration": start,"Goal Configuration": goal,"Runs": run_results})

                print ('\n----------------------------------------------------------')


                # Checking if the user wants to continue playing 
                answer = input('\nWould you like to continue playing the same game ??\n(YES/yes , NO/no)\nAnswer: ')
                if answer == 'YES' or answer == 'yes':
                    continue
                # If not the results are being printed  S
                else:
                    # Printing the measurements collectively
                    print ('\n----------------------------------------------------------')
                    for result in results:
                        print('\nStart Configuration:\n', BLUE + " ".join(str(result['Start Configuration'])) + RESET)
                        print('Goal Configuration:\n', BLUE + " ".join(str(result['Goal Configuration'])) + RESET)
                        for run_result in result['Runs']:
                            print('Algorithm:', MAGENTA + str(run_result['Algorithm']) + RESET, '| Runtime:', GREEN + str(run_result['Runtime']) + RESET, '| Expanded Nodes:', GREEN + str(run_result['Expanded Nodes']) + RESET)
                    print ('\n----------------------------------------------------------')

                    print('\nThanks for playing !!')
                    break


        # Choosing The Knight Problem
        elif answer == '4' or answer == 'The Knight Problem':
            while(True):
                # N x N chessboard
                N = 64  

                # Initializing another list that will keep track of 8-Puzzle information
                run_results = []            

                # Picking a random x variable for the starting possition of the pawn
                start_x = random.randint(0, N - 1)
                # Picking a random y variable for the starting possition of the pawn
                start_y = random.randint(0, N - 1)

                # Starting possition on the chessboard
                start = Knight_Node(start_x, start_y)
                #start_x = Knight_Node(0, N - 1)
                # Goal possition on the chessboard
                goal = Knight_Node(N-1, 0)   
            
                print('\nCalculating the minimum number of steps requared for the Knight to reach its goal with BFS, DFS, A*, B&B and IDS algorithms')

                # Calculating the minimum number of steps with BFS
                print ('\nBFS\n')
                start_time = time()
                bfs(start, goal, N)
                end_time = time()

                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number of initialized node: %d' % Knight_Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "BFS", "Runtime": elapsed,"Expanded Nodes": Knight_Node.n})

                print ('\n----------------------------------------------------------')

                # Calculating the minimum number of steps with DFS
                print ('\nDFS\n')
                start_time = time()
                dfs(start, goal, N)
                end_time = time()

                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number of initialized node: %d' % Knight_Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "DFS", "Runtime": elapsed,"Expanded Nodes": Knight_Node.n})

                print ('\n----------------------------------------------------------')

                # Calculating the minimum number of steps with A* (Manhattan Distance)
                print ('\nA* (Manhattan Distance)\n')
                start_time = time()
                astar_md(start, goal, N)
                end_time = time()

                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number of initialized node: %d' % Knight_Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "A* (Manhattan Distance)", "Runtime": elapsed,"Expanded Nodes": Knight_Node.n})

                print ('\n----------------------------------------------------------')

                # Calculating the minimum number of steps with A* (Manhattan Distance with Reversal Penalty)
                print ('\nA* (Manhattan Distance plus Reversal Penalty)\n')
                start_time = time()
                astar_mdrp(start, goal, N)
                end_time = time()

                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number of initialized node: %d' % Knight_Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "A* (Manhattan Distance plus Reversal Penalty)", "Runtime": elapsed,"Expanded Nodes": Knight_Node.n})

                print ('\n----------------------------------------------------------')

                # Calculating the minimum number of steps with B&B
                print ('\nB&B\n')
                start_time = time()
                b_and_b(start, goal, N)
                end_time = time()

                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number of initialized node: %d' % Knight_Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "B&B", "Runtime": elapsed,"Expanded Nodes": Knight_Node.n})

                print ('\n----------------------------------------------------------')

                # Calculating the minimum number of steps with IDS
                print ('\nIDS\n')
                start_time = time()
                ids(start, goal, N, 0)
                end_time = time()

                # Keeping track of the run time and the initialized nodes
                elapsed = end_time - start_time
                print ('Search time: %s' % elapsed)
                print ('Number of initialized node: %d' % Knight_Node.n)

                # Inserting the information to the list for a collective print later
                run_results.append({"Algorithm": "IDS", "Runtime": elapsed,"Expanded Nodes": Knight_Node.n})

                # Inserting further information to the other list for the collective print
                results.append({"Starting position": start,"Goal position": goal,"Runs": run_results})

                print ('\n----------------------------------------------------------')


                # Checking if the user wants to continue playing 
                answer = input('\nWould you like to continue playing the same game ??\n(YES/yes , NO/no)\nAnswer: ')
                if answer == 'YES' or answer == 'yes':
                    continue
                # If not the results are being printed  S
                else:
                    # Printing the measurements collectively
                    print ('\n----------------------------------------------------------')
                    for result in results:
                        print('\nStarting position:\n', BLUE + '(' + str(result['Starting position'].x) + ', ' + str(result['Starting position'].y) + ')' + RESET)
                        print('Goal position:\n', BLUE + '(' + str(result['Goal position'].x) + ', ' + str(result['Goal position'].y) + ')' + RESET)
                        for run_result in result['Runs']:
                            print('Algorithm:', MAGENTA + str(run_result['Algorithm']) + RESET, '| Runtime:', GREEN + str(run_result['Runtime']) + RESET, '| Expanded Nodes:', GREEN + str(run_result['Expanded Nodes']) + RESET)
                    print ('\n----------------------------------------------------------')

                    print('\nThanks for playing !!')
                    break

        # Choosing to exit the program
        elif answer == '5' or answer == 'Exit':
            break


        # A message in case the user doesnt choose one of the available games
        else:
            print('That is not a valid option, please try again.')