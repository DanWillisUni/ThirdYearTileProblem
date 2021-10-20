# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:22:08 2021

@author: danny
"""

import time
import copy
from Helpers import getAllMoves,makeMove,isOpposite,printFinal

def dfs_rec(currentState,path:list,goalState,maxDepth):
    if(currentState[2]==goalState[2]):
        return path;
    elif(len(path) < maxDepth):
        possibleMoves = getAllMoves(currentState)
        for m in possibleMoves:   
            lastMove = ''
            if(len(path)>0):
                lastMove = path[len(path) - 1]
            if not(isOpposite(m,lastMove)):
                cscopy = copy.deepcopy(currentState)
                pathcopy = copy.deepcopy(path)
                makeMove(cscopy,m)
                pathcopy.append(m)    
                solution = dfs_rec(cscopy,pathcopy, goalState,maxDepth)
                if(solution != None):
                    return solution
    return None        

def DFSgo(start,goal):
    print("{0} to {1}".format(start,goal))
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