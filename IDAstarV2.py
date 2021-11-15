# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:17:04 2021
@author: danny
"""

import time#import for timing
import copy#import for deepcopying
from Helpers import getAllMoves,makeMove,printFinal

def evaluateDif(previousState,direction): 
    """
    evaluate the difference to the current score that was made with the move
    Parameters
    ----------
    previousState : []
        state of the problem before the move
    direction : string
        direction to be moved
    Returns
    -------
    int
        the increase (can be negative) in the score if the move was made from previousState in the direction given
    """
    global goalState
    #set the difference in coordinates of the blank tile
    newY = 0
    newX = 0
    if(direction == "N"):#if direction is north
        newY = - 1
    elif(direction == "S"):#if direction moved is south
        newY = 1
    elif(direction == "E"):#if direction moved is East
        newX = 1
    elif(direction == "W"):#if direction moved is west
        newX = - 1
        
    count = 1 # set to one because a move costs one
    if(previousState[2][previousState[0] + newY][previousState[1] + newX] == goalState[2][previousState[0]][previousState[1]]):#non zero moves to where it should be
        count = count - 1#subtracts one from score as a tile has been moved to the correct location
    if(goalState[1] == previousState[1] + newX and goalState[0] == previousState[0] + newY):#zero moves to where it should be
        count = count - 1#subtracts one from score as a tile has been moved to the correct location
    if(previousState[2][previousState[0] + newY][previousState[1] + newX] == goalState[2][previousState[0] + newY][previousState[1]+ newX]):#non zero moves out of where it should be
        count = count + 1#add one to the score because A tile has been moved out of the correct location
    if(goalState[0] == previousState[0] and goalState[1] == previousState[1]):#zero moves out of where it should be
        count = count + 1#add one to the score because A tile has been moved out of the correct location
    return count#return the difference

def as_rec(currentScore,node,path,bound):
    """
    Searches the node and expands its children, if they have a low enough score it will recursivly call this function of them until a solution is found
    
    Parameters
    ----------
    currentScore : int
        score of the current state
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
    global movesExamined
    movesExamined = movesExamined + 1#add one to the moves counter
    global goalState
    if(node==goalState):#if the current state is the goalstate
        return path#set the solution to the item poppeds path
    else:#not the goal state
        lastMove = ''#set last move to empty incase it is the first move
        if(len(path)>0):#if the length of the path is greater than 0
            lastMove = path[len(path) - 1]#set the lastMove to the last move direction
        possibleMoves = getAllMoves(node,lastMove)#get all possible moves
        for m in possibleMoves:#for each possible move
            potentialScore = currentScore + evaluateDif(node,m)#get potential score
            if potentialScore <= bound:#if the score of the node is less than or equal to the max allowed          
                cscopy = copy.deepcopy(node)#copy current state
                pathcopy = copy.deepcopy(path)#copy current path
                makeMove(cscopy,m)#make the move on the copy of the current state
                pathcopy.append(m)#add the direction moved to the copy of the path 
                solution = as_rec(potentialScore,cscopy,pathcopy,bound)#recursive
                if(solution != None):#if that branch returned something other than None return the solution
                        return solution#return the solution that was found further down the line
    return None#no solution found down the path                 
        
         
def evaluateStartScore(currentState):
    """
    evaluate number of tiles that are in the wrong place
    
    used at the start to get the base score but from then on it is more efficient to use the evaluateDif function
    Parameters
    ----------
    currentState : []
        current state of the problem   
    Returns
    -------
    int
        the number of incorrect tiles in the grid
    """
    global goalState
    count = 0#score is initially set to 0
    for i in range(len(currentState[2])):#for Y axis
        for j in range(len(currentState[2][i])):#for X axis
            if(currentState[2][i][j]!=goalState[2][i][j]):#if a tile is in the wrong place
                count = count + 1#add one to the score
    return count
        
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
    print("{0} to {1}".format(start,goal))#print start and goal states  
    solution = None
    global movesExamined
    movesExamined = 0#set moves to 0  
    global goalState
    goalState = goal#set the global goalState to the goal
    t_start = time.process_time()#start the timer
    startScore = evaluateStartScore(start)#get the evaluation of the minimum moves to make it to the goal
    bound = startScore#set the depth to the starting evaluation
    while solution == None:#while a solution isnt found
        solution = as_rec(startScore,start,[],bound)#attempt to find a solution at this depth       
        bound = bound + 1#increase depth
    t_stop = time.process_time()#stop the timer
    printFinal(t_stop-t_start,solution,movesExamined)#print the info about the solution
    
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