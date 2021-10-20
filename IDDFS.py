# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:22:08 2021

@author: danny
"""

import time
import copy
from State import State
from Helpers import isOpposite,printFinal

def dfs_rec(currentState,path:list,goalState,maxDepth):
    if(currentState.grid==goalState.grid):
        return path;
    elif(len(path) < maxDepth):
        possibleMoves = currentState.getAllMoves()
        for m in possibleMoves:   
            lastMove = ''
            if(len(path)>0):
                lastMove = path[len(path) - 1]
            if not(isOpposite(m,lastMove)):
                cscopy = copy.deepcopy(currentState)
                pathcopy = copy.deepcopy(path)
                cscopy.makeMove(m)
                pathcopy.append(m)    
                solution = dfs_rec(cscopy,pathcopy, goalState,maxDepth)
                if(solution != None):
                    return solution
    return None        

def DFSgo(startState,goalState):
    print("{0} to {1}".format(startState,goalState))
    start = State(startState)
    goal = State(goalState)
    found = False
    depth = 1
    solution = list()
    t0 = time.time()
    while found == False:
        solution = dfs_rec(start,list(),goal,depth)
        if(solution != None):
            found = True
        else:
            depth = depth + 1
    t1 = time.time()  
    printFinal(t1-t0,solution)