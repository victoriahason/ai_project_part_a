def manhattan_distance(coord, targetcoord):
    return (abs(targetcoord.r-coord.r)+ abs(targetcoord.c-coord.c))

def get_adjacent_availalable_coords(coord):
    for i in [ Coord((coord.r)+1, coord.y), Coord((coord.r)-1, coord.y), Coord(coord.r, (coord.y)+1), Coord(coord.r+1, (coord.y)-1)]:
        ##If it is in the inital board dictionary or has been placed already, remove it as an option?
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

def closest_distance_to_r_or_c(x, target):
    return min(abs((target.c)-(x.c)), abs((target.r)-(x.r)))

def find_best_coord(board,startingcoord, target):
    check = False
    x = 1000
    adjacentsquares = [(startingcoord + Direction.Down), (startingcoord + Direction.Up), (startingcoord + Direction.Left), (startingcoord + Direction.Right)]
    for square in adjacentsquares:
        if not(square in board): #the square can't be already coloured, so if its in the board we dont consider it
             f = closest_distance_to_r_or_c(square, target)
             if f<x : ##return the square with the smallest f value
                 ret = square
                 check = True
                 x = f
    if check: ##basically, if you are able to find a coord that works. if you're blocked you need to backtrack :(
        board[ret] = PlayerColor.RED
        return ret 
    else:
        return 1

def find_best_coord2(board,tester,target, prev):
    check = False
    x = 1000
    adjacentsquares = [(tester + Direction.Down), (tester + Direction.Up), (tester + Direction.Left), (tester + Direction.Right)]
    for square in adjacentsquares:
        if not((square in board) or (square in prev)): #the square can't be already coloured, so if its in the board we dont consider it
             f = closest_distance_to_r_or_c(square, target)
             if f<x : ##return the square with the smallest f value
                 ret = square
                 check = True
                 x = f
    if check: ##basically, if you are able to find a coord that works. if you're blocked you need to backtrack :(
        return ret 
    else:
        return 1

      
def find_best_placeaction(board, startingcoord, target):
    coord1 = find_best_coord(board, startingcoord, target)
    coord2 = find_best_coord(board, coord1, target)
    coord3 = find_best_coord(board, coord2, target)
    coord4 = find_best_coord(board, coord3, target)
    return PlaceAction(coord1, coord2, coord3, coord4)

def find_best_placeaction_cost(board, tester, target):
    wrong = False
    prev = []
    coord1 = find_best_coord2(board, tester, target, prev)
    if coord1==1:
        return 100
    prev.append(coord1)
    coord2 = find_best_coord2(board, coord1, target, prev)
    if coord2==1:
        return 100
    prev.append(coord2)
    coord3 = find_best_coord2(board, coord2, target, prev)
    if coord3==1:
        return 100
    prev.append(coord3)
    coord4 = find_best_coord2(board, coord3, target, prev)
    if coord4==1:
        return 100
    prev.append(coord4)
    
    return how_many_target_squares_are_left_unfilled(board, prev, target)

#this finds how many squares in the board are left unfilled after your move
def how_many_target_squares_are_left_unfilled(board, move, target):
     count1 = 0
     count2 = 0
     
     for coord in move:
        if coord.r == target.r:
            count1 = count1+1
        if coord.c == target.c:
            count2 = count2+1

     return min((11-count1), (11-count2))

def search4(board, target) -> list:
    initialboard = copy.deepcopy(board)
    gscores = dict()
    solution = [] #Initialse solution list
    pq = PriorityQueue() #initialize priority queue

   ##Initializing##
    for coord,color in board.items():
        if color == PlayerColor.RED:
            gscores[coord]=0 #initialize all the gscores to 0
            h = closest_distance_to_r_or_c(coord, target)  ##maybe make it add the number of obstacles in the way? maybe add 1 for every obstacle in the way
            pq.put((h,coord))

    while not pq.empty():
        startingcoord = pq.get()[1]
        print (startingcoord)
        newblock= find_best_placeaction(board, startingcoord, target)
        print("hi")
        print(type(newblock))
        print(newblock.coords)
        solution.append(newblock)
        children = newblock.coords #get the coords of the place action, children is a list of coords

        if goaltest(initialboard, solution, target):
            return solution

        for next in children:
            newgscore = gscores[startingcoord] + 1 #or 4?
            if ((next not in gscores) or (newgscore < gscores[next])):
                gscores[next] = newgscore
                #bestchildcost = find_best_placeaction_cost(board, next, target)
                h2 = closest_distance_to_r_or_c(next, target)
                #heuristic = h2 + bestchildcost
                pq.put((newgscore+h2,next))



def search2(board, target) -> list:
   
    initialboard = copy.deepcopy(board)
    gscores = dict()
    solution = [] #Initialse solution list
    pq = PriorityQueue() #initialize priority queue

   ##Initializing##
    for coord,color in board.items():
        if color == PlayerColor.RED:
            gscores[coord]=0 #initialize all the gscores to 0
            h = closest_distance_to_r_or_c(coord, target)  ##maybe make it add the number of obstacles in the way? maybe add 1 for every obstacle in the way
            pq.put((h,coord))

    while not pq.empty():
        startingcoord = pq.get()[1]
        newblock= find_best_placeaction(board, startingcoord, target)
        print("hi")
        print(type(newblock))
        print(newblock.coords)
        solution.append(newblock)
        children = newblock.coords #get the coords of the place action, children is a list of coords

        if goaltest(initialboard, solution, target):
            return solution

        for next in children:
            newgscore = gscores[startingcoord] + 1 #or 4?
            if ((next not in gscores) or (newgscore < gscores[next])):
                gscores[next] = newgscore
                h = closest_distance_to_r_or_c(next, target)
                pq.put((h+newgscore,next))


def search3(board, target) -> list:
    initialboard = copy.deepcopy(board)
    gscores = dict()
    solution = [] #Initialse solution list
    pq = PriorityQueue() #initialize priority queue

   ##Initializing##
    for coord,color in board.items():
        if color == PlayerColor.RED:
            gscores[coord]=0 #initialize all the gscores to 0
            h = closest_distance_to_r_or_c(coord, target)  ##maybe make it add the number of obstacles in the way? maybe add 1 for every obstacle in the way
            pq.put((h,coord))

    while not pq.empty():
        startingcoord = pq.get()[1]
        print (startingcoord)
        newblock= find_best_placeaction(board, startingcoord, target)
        print("hi")
        print(type(newblock))
        print(newblock.coords)
        solution.append(newblock)
        children = newblock.coords #get the coords of the place action, children is a list of coords

        if goaltest(initialboard, solution, target):
            return solution

        for next in children:
            newgscore = gscores[startingcoord] + 1 #or 4?
            if ((next not in gscores) or (newgscore < gscores[next])):
                gscores[next] = newgscore
                #bestchildcost = find_best_placeaction_cost(board, next, target)
                h2 = closest_distance_to_r_or_c(next, target)
                #heuristic = h2 + bestchildcost
                pq.put((newgscore+h2,next))