# COMP30024 Artificial Intelligence, Semester 1 2024
# Project Part A: Single Player Tetress

from .core import PlayerColor, Coord, PlaceAction
from .utils import render_board
from queue import PriorityQueue

def generatesuccessors(board): ##this returns a list of PLACE ACTIONS
    pass

def estimate_cost_totarget(board):
    pass

def goaltest(board, solution): ###Not sure what goal test should be: check the column and the row i assume. but how do u keep track of where ur peices are?
    pass

def calculaute_f(board):
    pass

def updateboard(board):
    pass #not sure if i need this?

def search(board: dict[Coord, PlayerColor], target: Coord) -> list[PlaceAction] | None:
    
    solution = [] #Initialse solution list
    pq = PriorityQueue() #initialize priority queue
    initial_state = board 

    pq.put(0, initial_state)  #putting the initial state in the queue, not sure if i sould use 0?
    
    while not pq.empty():
        best_state = pq.dequeue()
        for i in generatesuccessors(best_state): ##keep in mind that the type of i is placeaction!!!!!!!!!
            tester = solution.append(i)
            if (goaltest(board, tester)): ##Not sure about what goaltest should take as input
                return tester #return the solution
            else:
               value =calculate_f(i)
               pq.enqueue(i,value)




   
    return [
        PlaceAction(Coord(2, 5), Coord(2, 6), Coord(3, 6), Coord(3, 7)),
        PlaceAction(Coord(1, 8), Coord(2, 8), Coord(3, 8), Coord(4, 8)),
        PlaceAction(Coord(5, 8), Coord(6, 8), Coord(7, 8), Coord(8, 8)),
    ]



    """
    This is the entry point for your submission. You should modify this
    function to solve the search problem discussed in the Part A specification.
    See `core.py` for information on the types being used here.

    Parameters:
        `board`: a dictionary representing the initial board state, mapping
            coordinates to "player colours". The keys are `Coord` instances,
            and the values are `PlayerColor` instances.  
        `target`: the target BLUE coordinate to remove from the board.
    
    Returns:
        A list of "place actions" as PlaceAction instances, or `None` if no
        solution is possible.
    """