# COMP30024 Artificial Intelligence, Semester 1 2024
# Project Part A: Single Player Tetress
# python -m search < test-vis1.csv
# python -m search < test-vis2.csv



##can i import directoin??##
from .core import PlayerColor, Coord, PlaceAction, Direction
from .utils import render_board
from queue import PriorityQueue
from .node import Node

def heuristic(board, target):
    count1 = 0
    count2 = 0
     
    for coord,color in board.items():
        if coord.r == target.r:
            count1 = count1+1
        
        if coord.c == target.c:
            count2 = count2+1

    return min((11-count1), (11-count2))


def search(board, target) -> list:

    ##make sure to implement clearing a column or row, in your evaluating each state!!! this can be in your generate successors maybe??
   
    initialboard = board
    solution = [] 
    pq = PriorityQueue()
    initialstate = Node(initialboard, None)
    initialstate.update_g(0)
    pq.put((0, initialstate))
    
    while not pq.empty():
        beststate = pq.get()[1]
        solution.append(beststate.pa)

        if beststate.goaltest(target):
            del solution[0]
            return solution
            
        
        pa = beststate.get_successor_placeactions(solution)
        successors = beststate.get_successor_states(pa)
   

        for successor in successors:  ###how do i keep track of the successors and not create a new one each time????? like if i reach a node ive already seen???
            newgscore = beststate.g + 1
            if (newgscore < successor.g):
                successor.g = newgscore
                h = heuristic(successor.state, target)
                pq.put((h+newgscore,successor))
    return None