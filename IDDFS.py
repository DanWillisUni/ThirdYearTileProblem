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

def go(start,goal):
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

for i in a:
    go(i,goala)
for i in b: 
    go(i,goalb)
print("Done")