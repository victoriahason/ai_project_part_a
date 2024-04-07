from .core import PlayerColor, Coord, PlaceAction, Direction
import copy

class Node:
    def __init__(self, board, pa):
        self.state = board
        self.g = float('inf')
        self.pa = pa
    
    def __lt__(self, other):
        return self.g < other.g  # Compare based on the g value
    
    def __eq__(self, other):
        return self.state == other.state
    
    def update_g(self, g):
        self.g =g
    
    def set_parent(self, node):
        self.parent = node

    
    def get_successor_placeactions(self, solution):
        directions = [Direction.Up, Direction.Down, Direction.Left, Direction.Right]
        placeactions = []

        ##maybe i should do for d2 in directions - d1???? just cause here i can have 2 of the same coordinates????
        ## of i can just remove any placeaction that contains 2 of the same coordinates
        
        for coord,color in self.state.items():
        #for coord in self.pa
            if color == PlayerColor.RED: 
                
                for d1 in directions:
                    b1 = coord + d1
                    if b1 in self.state:
                        continue
                    
                    for d2 in directions:
                        b2 = b1 + d2
                        if (b2 in self.state) or (b2 == coord):
                            continue
                        
                        for d3 in directions:
                            b3 = b2 + d3
                            if (b3 in self.state) or (b3 == b1) or (b3 == coord):
                                continue
                            
                            for d4 in directions:
                                b4 = b3 + d4
                                if (b4 in self.state) or (b4 == b2) or (b4 == b1) or (b4 == coord):
                                    continue
                                else: #this means you can oficially make a place action
                                    possiblemove = PlaceAction(b1, b2, b3, b4)
                                    placeactions.append(possiblemove)
        return placeactions
    
    def get_successor_states(self, pa):
        states = []
        possiblemoves = pa
        for move in possiblemoves:
            newboard = copy.deepcopy(self.state)
            for block in move.coords:
                newboard[block] = PlayerColor.RED
            newnode = Node(newboard, move)
            newnode.check_and_clear()
            states.append(newnode)
        return states
    
    def check_and_clear(self):
        for i in range(11):
            row_filled = all(Coord(i, j) in self.state for j in range(11))
            if row_filled:
                print(f"row cleared is: {i}")
                for j in range(11):
                    pass
                    #del self.state[Coord(i, j)]
                    

        for j in range(11):
            col_filled = all(Coord(i, j) in self.state for i in range(11))
            if col_filled:
                print(f"column cleared is: {j}")
                for i in range(11):
                    pass
                    #del self.state[Coord(i, j)]
                    

    def goaltest(self, target):
        ccheck = True
        rcheck = True
    
        for c in range (11):
            if not(Coord(target.r, c) in self.state):
                ccheck = False

        for r in range (11):
            if not (Coord(r, target.c) in self.state):
                rcheck = False
    
        return (ccheck or rcheck)



