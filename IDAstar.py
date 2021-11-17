# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:17:04 2021
@author: danny

OUTPUT

[0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]] to [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
Time was:     0.00 seconds
Solution was:  ['E', 'S', 'W', 'S', 'E', 'N', 'W', 'N', 'E', 'E', 'S', 'W', 'W', 'S', 'E', 'N', 'N', 'E']
Length:  18
Moves yielded:  234

[0, 2, [[5, 6, 0], [1, 3, 8], [4, 7, 2]]] to [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
Time was:     0.05 seconds
Solution was:  ['W', 'W', 'S', 'E', 'E', 'S', 'W', 'N', 'N', 'E', 'S', 'W', 'S', 'E', 'N', 'W', 'N', 'W', 'S', 'E', 'N', 'E']
Length:  22
Moves yielded:  1443

[2, 0, [[3, 5, 6], [1, 2, 7], [0, 8, 4]]] to [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
Time was:     0.14 seconds
Solution was:  ['E', 'E', 'N', 'N', 'W', 'S', 'W', 'S', 'E', 'N', 'W', 'N', 'E', 'S', 'E', 'N', 'W', 'W', 'S', 'E', 'S', 'E', 'N', 'N']
Length:  24
Moves yielded:  5940

[1, 1, [[7, 3, 5], [4, 0, 2], [8, 1, 6]]] to [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
Time was:     0.48 seconds
Solution was:  ['W', 'S', 'E', 'N', 'W', 'N', 'E', 'S', 'E', 'N', 'W', 'S', 'S', 'W', 'N', 'E', 'S', 'E', 'N', 'W', 'S', 'W', 'N', 'E', 'E', 'N']
Length:  26
Moves yielded:  22463

[2, 0, [[6, 4, 8], [7, 1, 3], [0, 2, 5]]] to [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
Time was:     0.02 seconds
Solution was:  ['N', 'E', 'N', 'W', 'S', 'E', 'S', 'W', 'N', 'N', 'E', 'S', 'E', 'N', 'W', 'S', 'W', 'N', 'E', 'E']
Length:  20
Moves yielded:  1823

[0, 0, [[0, 1, 8], [3, 6, 7], [5, 4, 2]]] to [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
Time was:     0.00 seconds
Solution was:  ['E', 'S', 'W', 'S', 'E', 'E', 'N', 'N', 'W', 'S', 'S', 'E', 'N', 'N', 'W', 'S', 'W', 'S', 'E', 'E']
Length:  20
Moves yielded:  187

[2, 0, [[6, 4, 1], [7, 3, 2], [0, 5, 8]]] to [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
Time was:     0.00 seconds
Solution was:  ['N', 'N', 'E', 'E', 'S', 'W', 'W', 'N', 'E', 'E', 'S', 'W', 'S', 'E']
Length:  14
Moves yielded:  39

[0, 0, [[0, 7, 1], [5, 4, 8], [6, 2, 3]]] to [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
Time was:     0.05 seconds
Solution was:  ['E', 'S', 'E', 'S', 'W', 'W', 'N', 'N', 'E', 'E', 'S', 'W', 'S', 'E', 'N', 'W', 'S', 'W', 'N', 'N', 'E', 'S', 'S', 'E']
Length:  24
Moves yielded:  2665

[0, 2, [[5, 4, 0], [2, 3, 1], [8, 7, 6]]] to [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
Time was:     0.11 seconds
Solution was:  ['W', 'S', 'E', 'N', 'W', 'S', 'W', 'N', 'E', 'S', 'S', 'W', 'N', 'E', 'E', 'S', 'W', 'W', 'N', 'E', 'S', 'E']
Length:  22
Moves yielded:  5056

[2, 1, [[8, 6, 7], [2, 5, 4], [3, 0, 1]]] to [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
Time was:     0.84 seconds
Solution was:  ['E', 'N', 'W', 'W', 'S', 'E', 'E', 'N', 'N', 'W', 'W', 'S', 'E', 'N', 'W', 'S', 'S', 'E', 'E', 'N', 'W', 'S', 'E', 'N', 'N', 'W', 'W', 'S', 'S', 'E', 'E']
Length:  31
Moves yielded:  36345

Done in     1.72 seconds
"""

import time#import for timing
import copy#import for deepcopying

def successors(state,lastMove):
    """
    Gets the allowed move directions from the current state

    Ignores a move if it would take it back to the previous state
    EG: if the last move was West it would not return East

    Parameters
    ----------
    state : []
        current state of the problem
    lastMove : str
        Direction that was last moved

    Returns
    -------
    []
        The directions that are possible to move from based on the current state

    """
    global movesYielded#the number of moves yielded by this function
    allowedMoves = [] #I discovered that a list was more efficient that yielding a next state
    if(state[1] !=len(state[2][0]) - 1 and lastMove != "W"):#if the player can move east and west wasnt the last move
        allowedMoves.append("E")#add east to direction list
    if(state[1] !=0 and lastMove != "E"):#if the player can move west and east wasnt the last move
        allowedMoves.append("W")#add west to direction list
    if(state[0] !=len(state[2])-1 and lastMove != "N"):#if the player can move south and north wasnt the last move
        allowedMoves.append("S")#add south to direction list
    if(state[0] !=0 and lastMove !="S"):#if the player can move north and south wasnt the last move
        allowedMoves.append("N")#add north to direction list
    movesYielded = movesYielded + len(allowedMoves)#add one to the moves counter
    return allowedMoves#return the list

def makeMove(state,direction):
    """
    Transforms the state by making a move in the direction    

    Parameters
    ----------
    state : []
        current state of the problem
    directione : str
        Direction that needs to be moved

    Returns
    -------
    []
        The state after being transormed by the move in the direction

    """    
    newBlankX = state[1]#set the new blank X coord to the old
    newBlankY = state[0]#set the new blank Y coord to the old
    if(direction == "N"):#if the direction is north
        newBlankY = state[0] - 1#set the newBlankY location one higher
    elif(direction == "S"):#if the direction is south
        newBlankY = state[0] + 1#set the new blank tile Y coord one lower
    elif(direction == "E"):#if the direction is east        
        newBlankX = state[1] + 1#set the new blank tile X coord one right
    elif(direction == "W"):#if the direction is west
        newBlankX = state[1] - 1#set the new blank tile X coord one left
    #make the move on the state
    state[2][state[0]][state[1]] = state[2][newBlankY][newBlankX]#set the tile that swapped with the 0
    state[2][newBlankY][newBlankX] = 0#set the new 0
    state[0] = newBlankY#set the new states blank tile Y coords
    state[1] = newBlankX#set the new states blank tile X coords

def as_rec(node,path,bound):
    """
    Searches the node and expands its children, if they have a low enough score it will recursivly call this function of them until a solution is found
    
    Parameters
    ----------
    node : []
        state of the problem
    path : []
        directions moved to get from the root to the current state
    bound : int
        the max score a node can get to be expanded
    Returns
    -------
    []
        If a solution is found without going over the max depth then the directions are returned in an array, otherwise None
    """    
    global goalState#the goal state of the problem
    global minBoundFound#the minimum score found that is over bound 
    global movesYielded#the number of moves yielded by the successors function
    if(node==goalState):#if the current state is the goalstate
        return path#return the path that got to current state
    else:#not the goal state
        lastMove = ''#set last move to empty incase it is the first move
        if(len(path)>0):#if the length of the path is greater than 0
            lastMove = path[len(path) - 1]#set the lastMove to the last move direction
            movesYielded = movesYielded + 1#add one here because successor function will ignore the opposite of the previous move
        possibleMoves = successors(node,lastMove)#get all successsors
        for m in possibleMoves:#for each possible move
            cscopy = copy.deepcopy(node)#copy current state                
            makeMove(cscopy,m)#make the move on the copy of the current state
            potentialScore = len(path) + 1 + h(cscopy)#get potential score using len(path) + 1 (plus one is because the move hasnt been added to the path yet) as the current cost to save on a deep copy of the path if the score is higher than bound
            if potentialScore <= bound:#if the score of the node is less than or equal to the max allowed          
                pathcopy = copy.deepcopy(path)#copy current path
                pathcopy.append(m)#add the direction moved to the copy of the path 
                solution = as_rec(cscopy,pathcopy,bound)#set the solution to the return of the child
                if(solution != None):#if that branch returned something other than None
                    return solution#return the solution that was found further down the tree
            elif potentialScore < minBoundFound:#else if the score is lower than any previously found but still over the bound 
                minBoundFound = potentialScore#set the minimum found score to the potential score
    return None#no solution found down the path 
         
def h(currentState):
    """
    The sum of Manhatten distance of the numbered tiles
    
    The evaluation of a tile is the Manhattan distance between its position in the current state and its position in the goal state.
    
    Parameters
    ----------
    currentState : []
        current state of the problem  
    Returns
    -------
    int
        the sum of the minimun the tiles have to move to get to the correct location
    """
    global goalState#goal state of the problem
    count = 0#score is initially set to 0
    for i in range(len(currentState[2])):#for Y axis
        for j in range(len(currentState[2][i])):#for X axis
            if currentState[2][i][j] != 0:#if it isnt the blank space
                found = False#found is false and is used to escape the goalState Y axis for loop
                for gi in range(len(goalState[2])):#for Y axis
                    for gj in range(len(goalState[2][i])):#for X axis
                        if currentState[2][i][j] == goalState[2][gi][gj]:#if they match
                            count = count + abs(i - gi) + abs(j - gj)#sum of the absolute value of the difference
                            found = True#the tile has been found
                            break#break the goalState x axis for loop
                    if found:#if found
                        break#break goalState y axis for loop
    return count#return the evaluation
        
def search(start,goal):
    """
    Solves from start to goal
    
    prints the solution and the time taken and the number of moves looked at
    Parameters
    ----------
    start : []
        start state of the problem    
    goal : []
        goal state of the problem    
    """
    global movesYielded#the moves returned from the successors
    global goalState#the goal state of the problem
    global minBoundFound#the minimum score found that is over bound
    print("{0} to {1}".format(start,goal))#print start and goal states  
    solution = None#initilize solution as null for the while loop condition
    movesYielded = 0#set moves to 0      
    goalState = goal#set the global goalState to the goal    
    minBoundFound = 10000#set minimum bound found really high
    t_start = time.process_time()#start the timer
    bound = h(start)#get the evaluation of the minimum moves to make it to the goal
    while solution == None:#while a solution isnt found
        solution = as_rec(start,[],bound)#attempt to find a solution at this depth       
        bound = minBoundFound#increase depth
        minBoundFound = 10000#set minimum high again
    t_stop = time.process_time()#stop the timer
    print("Time was: {:8.2f} seconds".format(t_stop-t_start))#print the time taken
    print("Solution was: ",solution)#print the directions moved
    print("Length: ",str(len(solution)))#print the number of moves taken
    print("Moves yielded: ",movesYielded)#print the number pf moves looked at
    print()#print blank line to split up the solutions
    
#set start states and goal states
a = [[0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]],
[0, 2, [[5, 6, 0], [1, 3, 8], [4, 7, 2]]],
[2, 0, [[3, 5, 6], [1, 2, 7], [0, 8, 4]]],
[1, 1, [[7, 3, 5], [4, 0, 2], [8, 1, 6]]],
[2, 0, [[6, 4, 8], [7, 1, 3], [0, 2, 5]]]]
goala = [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]

b = [[0, 0, [[0, 1, 8], [3, 6, 7], [5, 4, 2]]],
[2, 0, [[6, 4, 1], [7, 3, 2], [0, 5, 8]]],
[0, 0, [[0, 7, 1], [5, 4, 8], [6, 2, 3]]],
[0, 2, [[5, 4, 0], [2, 3, 1], [8, 7, 6]]],
[2, 1, [[8, 6, 7], [2, 5, 4], [3, 0, 1]]]]
goalb = [2,2,[[1,2,3],[4,5,6],[7,8,0]]]

t_start = time.process_time()#start the timer
for i in a:#for all first set of start states
    search(i,goala)#solve with first goal
for i in b:#for all second set of start states
    search(i,goalb)#solve for second goal
t_stop = time.process_time()#stop the timer
print("Done in {:8.2f} seconds".format(t_stop-t_start))#print the time taken in total for the whole program