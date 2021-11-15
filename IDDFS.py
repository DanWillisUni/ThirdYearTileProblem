# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:22:08 2021

@author: danny
"""

import time#import for timing
import copy#import for deepcopying
from Helpers import getAllMoves,makeMove,printFinal

def dfs_rec(currentState,path:list,goalState,maxDepth):
    """
    DFS recursive function

    Parameters
    ----------
    currentState : []
        current state of the problem
    path : []
        directions moved from the start to get to the current state
    goalState : []
        goal state of the problem
    maxDepth : int
        current max depth of the solution

    Returns
    -------
    []
        If a solution is found without going over the max depth then the directions are returned in an array, otherwise None

    """
    global moves#global number of moves examined 
    if(currentState[2]==goalState[2]):#if the current state is the goal state
        return path #return the solution
    elif(len(path) < maxDepth):#else if the path isnt at the max depth yet
        lastMove = ''#set to blank char for first move
        if(len(path)>0):#if it isnt the first move
            lastMove = path[len(path) - 1]#set the last move direction
        possibleMoves = getAllMoves(currentState,lastMove)#get all the possible moves from the current state that wont go back to the previous state
        for m in possibleMoves:#for all possible moves
            moves = moves + 1#add one to the number of moves examined counter
            cscopy = copy.deepcopy(currentState)#copy state
            pathcopy = copy.deepcopy(path)#copy path
            makeMove(cscopy,m)#make the move on the state copy
            pathcopy.append(m)#add the move to the path array  
            solution = dfs_rec(cscopy,pathcopy, goalState,maxDepth)#recursivly call with the new state and new path
            if(solution != None):#if that branch returned something other than None return the solution
                return solution#return the solution that was found further down the line
    return None#no solution found down the path

def go(start,goal):
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
    found = False
    depth = 1#start at a depth of 1
    solution = None
    global moves
    moves = 0#set moves to 0
    t_start = time.process_time()#start timer
    while solution == None:#while a solution isnt found
        solution = dfs_rec(start,[],goal,depth)#attempt to find a solution at this depth       
        depth = depth + 1#increase depth
    t_stop = time.process_time()#stop timer
    printFinal(t_stop-t_start,solution,moves)#print the info about the solution
    
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

for i in a:#for all first set of start states
    go(i,goala)#solve with first goal
for i in b:#for all second set of start states
    go(i,goalb)#solve for second goal
print("Done")