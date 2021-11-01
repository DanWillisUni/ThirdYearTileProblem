# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:22:08 2021

@author: danny
"""

from time import process_time
import copy
from Helpers import move,isOpposite,printFinal

def dfs_rec(path:list,goalState,maxDepth): 
    global moves
    if(path[len(path) - 1][2]==goalState[2]):
        return path;
    elif(len(path) < maxDepth):
        for m in move(path[len(path) - 1]):             
            moves = moves + 1
            skip = False
            if(len(path) > 2):           
                if(path[len(path) - 2] == m):
                    skip = True
            if(not skip):
                pathcopy = copy.deepcopy(path)
                pathcopy.append(m)                               
                solution = dfs_rec(pathcopy, goalState,maxDepth)
                if(solution != None):
                    return solution
    return None        

def go(start,goal):
    print("{0} to {1}".format(start,goal))
    found = False
    depth = 1
    solution = list()
    global moves
    moves = 0
    t_start = process_time() 
    while found == False:
        solution = dfs_rec([start],goal,depth)
        if(solution != None):
            found = True
        else:
            depth = depth + 1
    t_stop = process_time()
    printFinal(t_stop-t_start,solution,moves)
    
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