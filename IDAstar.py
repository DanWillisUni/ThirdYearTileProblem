# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:17:04 2021

@author: danny
"""

import time
import copy
import heapq
from Helpers import move,printFinal

def evaluateDif(previousState,nextstate,goalState): 
    count = 1
    if(nextstate[2][previousState[0]][previousState[1]] == goalState[2][previousState[0]][previousState[1]]):#non zero moves to where it should be
        count = count - 1
    if(goalState[1] == nextstate[1] and goalState[0] == nextstate[0]):#zero moves to where it should be
        count = count - 1
    if(previousState[2][nextstate[0]][nextstate[1]] == goalState[2][nextstate[0]][nextstate[1]]):#non zero moves out of where it should be
        count = count + 1
    if(goalState[0] == previousState[0] and goalState[1] == previousState[1]):#zero moves out of where it should be
        count = count + 1
    return count
        
def as_doNode(path,goalState,currentScore): 
    global h
    if(path[len(path) - 1]==goalState):
        return path;
    else:        
        for m in move(path[len(path) - 1]): 
            skip = False
            if(len(path) > 1):           
                if(path[len(path) - 2] == m):
                    skip = True
            if(not skip):
                potentialScore = currentScore + evaluateDif(path[len(path) - 1],m,goalState)
                pathcopy = copy.deepcopy(path)
                pathcopy.append(m) 
                heapq.heappush(h, (potentialScore, pathcopy))                
    return None
        
def evaluateStartScore(currentState,goalState):
    count = 0
    for i in range(len(currentState[2])):
        for j in range(len(currentState[2][i])):
            if(currentState[2][i][j]!=goalState[2][i][j]):
                count = count + 1
    return count
        
def go(start,goal):
    print("{0} to {1}".format(start,goal))    
    solution = None
    found = False  
    moves = 0
    global h  
    h = []
    t_start = time.process_time()
    heapq.heappush(h,(evaluateStartScore(start,goal),[start])) 
    while solution == None:
        item = heapq.heappop(h)
        solution = as_doNode(item[1], goal,item[0])
        moves = moves + 1
    t_stop = time.process_time()
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