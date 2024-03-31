class Node:
    def __init__(self, coord):
        self.coord = coord
        self.parent = None
        self.g = float('inf')
        self.h = 0
    
    ## two nodes are the same if they represent the same coordinate --> i have to make sure then that i can still update the g on one of them and it will be the same?
    def __eq__(self, other):
        return (self.r, self.c) == (other.r, other.c)

    def update_g(g):
        self.g =g
    
    def update_h(h):
        self.h = h

    def set_parent(node):
        self.parent = node
