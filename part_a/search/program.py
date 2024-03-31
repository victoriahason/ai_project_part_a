# COMP30024 Artificial Intelligence, Semester 1 2024
# Project Part A: Single Player Tetress

##can i import directoin??##
from .core import PlayerColor, Coord, PlaceAction, Direction
from node import Node
from .utils import render_board
from queue import PriorityQueue
import copy

def manhattan_distance(coord, targetcoord):
    return (abs(targetcoord.r-coord.r)+ abs(targetcoord.c-coord.c))

def relax(node1, node2):
    pass ##do i create a class node which has a field coord and a field value????????????

def get_adjacent_available_coords(coord):
    for i in [ Coord((coord.r)+1, coord.y), Coord((coord.r)-1, coord.y), Coord(coord.r, (coord.y)+1), Coord(coord.r+1, (coord.y)-1)]:
        ##If it is in the inital board dictionary or has been placed already, remove it as an option?
        pass

def generatesuccessors(board): ##this returns a list of PLACE ACTIONS
    pass

def estimate_cost_totarget(board):
    pass

def goaltest(initialboard, solution, target):
    # Create a copy of the board to simulate the actions
    board_copy = copy.deepcopy(initialboard)

    # Apply each place action in the solution to the board copy
    for action in solution:
        for coord in action.coords:
            board_copy[coord] = PlayerColor.RED

    # Check if the target coordinate's row or column is fully filled
    #basically, if at some point the target row or column does not have a number associated to it, then it hasn't been filled. In that case,
    ## it will not be in the board, so check becomes false. then one of the 2 or both is false.
            
    ccheck = True
    rcheck = True
    
    for c in range (11):
        if not(Coord(target.r, c) in board_copy):
            ccheck = False

    for r in range (11):
        if not (Coord(r, target.c) in board_copy):
            rcheck = False
    
    return (ccheck or rcheck)


def calculate_f(board):
    pass

def updateboard(board):
    pass #not sure if i need this?

def num_empty_squares_in_targt_rc(coord,solution):
    pass

def closest_distance_to_r_or_c(x, target):
    return min(abs((target.c)-(x.c)), abs((target.r)-(x.r)))

def find_best_coord(board,startingcoord, target):
    x = 1000
    adjacentsquares = [(startingcoord + Direction.Down), (startingcoord + Direction.Up), (startingcoord + Direction.Left), (startingcoord + Direction.Right)]
    for square in adjacentsquares:
        if not(square in board): #the square can't be already coloured, so if its in the board we dont consider it
             f = closest_distance_to_r_or_c(square, target)
             if f<x : ##return the square with the smallest f value
                 ret = square
                 x = f
    board[ret] = PlayerColor.RED
    return ret          

      
def find_best_placeaction(board, startingcoord, target):
    coord1 = find_best_coord(board, startingcoord, target)
    coord2 = find_best_coord(board, coord1, target)
    coord3 = find_best_coord(board, coord2, target)
    coord4 = find_best_coord(board, coord3, target)
    return PlaceAction(coord1, coord2, coord3, coord4)


def search(board, target) -> list:
   
    initialboard = copy.deepcopy(board)
    gscores = dict()
    solution = [] #Initialse solution list
    pq = PriorityQueue() #initialize priority queue

   ##Initializing##
    for (coord,color) in board.items():
        if color == PlayerColor.RED:
            node = Node(coord)
            gscores[coord]=0 #initialize all the gscores to 0
            h = closest_distance_to_r_or_c(node.coord, target)  ##maybe make it add the number of obstacles in the way? maybe add 1 for every obstacle in the way
            pq.enqueue(node,h)

    while not pq.empty():
        startingcoord = pq.dequeue()
        newblock= find_best_placeaction(board, startingcoord, target)
        solution = solution.append(newblock)
        children = newblock.coords() #get the coords of the place action, children is a list of coords

        if goaltest(initialboard, solution, target):
            return solution

        for next in children:
            newgscore = gscores[startingcoord] + 1 #or 4?
            if ((next not in gscores) or (newgscore < gscores[next])):
                gscores[next] = newgscore
                h = closest_distance_to_r_or_c(next, target)
                pq.enqueue(node,h+newgscore)
    