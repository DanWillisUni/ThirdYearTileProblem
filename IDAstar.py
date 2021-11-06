# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:17:04 2021

@author: danny
"""

import time
import copy
import heapq
from Helpers import getAllMoves,makeMove,printFinal

def evaluateDif(previousState,direction,goalState):    
    newY = 0
    newX = 0
    if(direction == "N"):
        newY = - 1
    elif(direction == "S"):
        newY = 1
    elif(direction == "E"):
        newX = 1
    elif(direction == "W"):
        newX = - 1
        
    count = 1 # set to one because a move costs one
    if(previousState[2][previousState[0] + newY][previousState[1] + newX] == goalState[2][previousState[0]][previousState[1]]):#non zero moves to where it should be
        count = count - 1
    if(goalState[1] == previousState[1] + newX and goalState[0] == previousState[0] + newY):#zero moves to where it should be
        count = count - 1
    if(previousState[2][previousState[0] + newY][previousState[1] + newX] == goalState[2][previousState[0] + newY][previousState[1]+ newX]):#non zero moves out of where it should be
        count = count + 1
    if(goalState[0] == previousState[0] and goalState[1] == previousState[1]):#zero moves out of where it should be
        count = count + 1
    return count
         
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
    item = heapq.heappushpop(h,(evaluateStartScore(start,goal),start,[]))
    while solution == None:  
        if(item[1]==goal):
            solution = item[2];
        else:  
            lastMove = ''
            if(len(item[2])>0):
                lastMove = item[2][len(item[2]) - 1]
            possibleMoves = getAllMoves(item[1],lastMove)
            for m in possibleMoves:      
                potentialScore = item[0] + evaluateDif(item[1],m,goal)
                cscopy = copy.deepcopy(item[1])
                pathcopy = copy.deepcopy(item[2])
                makeMove(cscopy,m)
                pathcopy.append(m)    
                heapq.heappush(h, (potentialScore, cscopy,pathcopy))   
        moves = moves + 1
        item =  heapq.heappop(h)
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