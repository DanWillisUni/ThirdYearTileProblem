# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:22:08 2021

@author: danny

OUTPUT

[0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]] to [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
Time was:     2.53 seconds
Solution was:  ['E', 'S', 'W', 'S', 'E', 'N', 'W', 'N', 'E', 'E', 'S', 'W', 'W', 'S', 'E', 'N', 'N', 'E']
Length:  18
Moves yielded:  184319

[0, 2, [[5, 6, 0], [1, 3, 8], [4, 7, 2]]] to [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
Time was:    20.16 seconds
Solution was:  ['W', 'W', 'S', 'E', 'E', 'S', 'W', 'N', 'N', 'E', 'S', 'W', 'S', 'E', 'N', 'W', 'N', 'W', 'S', 'E', 'N', 'E']
Length:  22
Moves yielded:  1361634

[2, 0, [[3, 5, 6], [1, 2, 7], [0, 8, 4]]] to [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
Time was:    67.48 seconds
Solution was:  ['E', 'E', 'N', 'N', 'W', 'S', 'W', 'S', 'E', 'N', 'W', 'N', 'E', 'S', 'E', 'N', 'W', 'W', 'S', 'E', 'S', 'E', 'N', 'N']
Length:  24
Moves yielded:  4472793

[1, 1, [[7, 3, 5], [4, 0, 2], [8, 1, 6]]] to [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
Time was:   391.44 seconds
Solution was:  ['W', 'S', 'E', 'N', 'W', 'N', 'E', 'S', 'E', 'N', 'W', 'S', 'S', 'W', 'N', 'E', 'S', 'E', 'N', 'W', 'S', 'W', 'N', 'E', 'E', 'N']
Length:  26
Moves yielded:  20211530

[2, 0, [[6, 4, 8], [7, 1, 3], [0, 2, 5]]] to [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
Time was:    10.61 seconds
Solution was:  ['N', 'E', 'N', 'W', 'S', 'E', 'S', 'W', 'N', 'N', 'E', 'S', 'E', 'N', 'W', 'S', 'W', 'N', 'E', 'E']
Length:  20
Moves yielded:  713898

[0, 0, [[0, 1, 8], [3, 6, 7], [5, 4, 2]]] to [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
Time was:     8.20 seconds
Solution was:  ['E', 'S', 'W', 'S', 'E', 'E', 'N', 'N', 'W', 'S', 'S', 'E', 'N', 'N', 'W', 'S', 'W', 'S', 'E', 'E']
Length:  20
Moves yielded:  546047

[2, 0, [[6, 4, 1], [7, 3, 2], [0, 5, 8]]] to [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
Time was:     0.30 seconds
Solution was:  ['N', 'N', 'E', 'E', 'S', 'W', 'W', 'N', 'E', 'E', 'S', 'W', 'S', 'E']
Length:  14
Moves yielded:  26781

[0, 0, [[0, 7, 1], [5, 4, 8], [6, 2, 3]]] to [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
Time was:    73.97 seconds
Solution was:  ['E', 'S', 'E', 'S', 'W', 'W', 'N', 'N', 'E', 'E', 'S', 'W', 'S', 'E', 'N', 'W', 'S', 'W', 'N', 'N', 'E', 'S', 'S', 'E']
Length:  24
Moves yielded:  4571525

[0, 2, [[5, 4, 0], [2, 3, 1], [8, 7, 6]]] to [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
Time was:    25.56 seconds
Solution was:  ['W', 'S', 'E', 'N', 'W', 'S', 'W', 'N', 'E', 'S', 'S', 'W', 'N', 'E', 'E', 'S', 'W', 'W', 'N', 'E', 'S', 'E']
Length:  22
Moves yielded:  1609413

[2, 1, [[8, 6, 7], [2, 5, 4], [3, 0, 1]]] to [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
Time was:  3870.09 seconds
Solution was:  ['E', 'N', 'W', 'W', 'S', 'E', 'E', 'N', 'N', 'W', 'W', 'S', 'E', 'N', 'W', 'S', 'S', 'E', 'E', 'N', 'W', 'S', 'E', 'N', 'N', 'W', 'W', 'S', 'S', 'E', 'E']
Length:  31
Moves yielded:  219197131

Done in  4470.34 seconds
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

def dfs_rec(currentState,path,bound):
    """
    DFS recursive function
    
    Expands the child nodees of the current node if the max depth hasnt been reached and then recursively calls the function on each of the children

    Parameters
    ----------
    currentState : []
        current state of the problem
    path : []
        directions moved from the start to get to the current state
    bound : int
        current max depth of the solution

    Returns
    -------
    []
        If a solution is found without going over the max depth then the directions are returned in an array, otherwise None

    """    
    global goalState#the goal state of the problem
    global movesYielded#the number of movess yielded by the successors function
    if(currentState==goalState):#if the current state is the goal state
        return path #return the solution
    elif(len(path) <= bound):#else if the path isnt at the max depth yet
        lastMove = ''#set to blank char for first move
        if(len(path)>0):#if it isnt the first move
            lastMove = path[len(path) - 1]#set the last move direction
            movesYielded = movesYielded + 1#add one here because successor function will ignore the opposite of the previous move
        possibleMoves = successors(currentState,lastMove)#get all the possible moves from the current state that wont go back to the previous state
        for m in possibleMoves:#for all possible moves
            cscopy = copy.deepcopy(currentState)#copy state
            pathcopy = copy.deepcopy(path)#copy path
            makeMove(cscopy,m)#make the move on the state copy
            pathcopy.append(m)#add the move to the path array  
            solution = dfs_rec(cscopy,pathcopy, bound)#recursivly call with the new state and new path
            if(solution != None):#if that branch returned something other than None return the solution
                return solution#return the solution that was found further down the line
    return None#no solution found down the path

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
    global movesYielded
    global goalState
    print("{0} to {1}".format(start,goal))#print start and goal states
    bound = 1#start at a max depth of 1
    solution = None#set the solution to none    
    movesYielded = 0#set movesExamined to 0    
    goalState = goal#seeet the global goalState to goal
    t_start = time.process_time()#start timer
    while solution == None:#while a solution isnt found
        solution = dfs_rec(start,[],bound)#attempt to find a solution at this depth       
        bound = bound + 1#increase the max depth
    t_stop = time.process_time()#stop timer
    print("Time was: {:8.2f} seconds".format(t_stop-t_start))#print the time taken
    print("Solution was: ",solution)#print the directions moved
    print("Length: ",str(len(solution)))#print the number of moves taken
    print("Moves yielded: ",movesYielded)#print the number of moves looked at
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