# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:17:04 2021

@author: danny
"""

import time
import copy
from Helpers import getAllMoves,makeMove,isOpposite,printFinal
    
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
        
    count = 1
    if(previousState[2][previousState[0] + newY][previousState[1] + newX] == goalState[2][previousState[0]][previousState[1]]):#non zero moves to where it should be
        count = count - 1
    if(goalState[1] == previousState[1] + newX and goalState[0] == previousState[0] + newY):#zero moves to where it should be
        count = count - 1
    if(previousState[2][previousState[0] + newY][previousState[1] + newX] == goalState[2][previousState[0] + newY][previousState[1]+ newX]):#non zero moves out of where it should be
        count = count + 1
    if(goalState[0] == previousState[0] and goalState[1] == previousState[1]):#zero moves out of where it should be
        count = count + 1
    return count
        
def as_rec(currentState,path,goalState,maxDepth,currentScore):
    if(currentState[2]==goalState[2]):
        return path;
    else:
        possibleMoves = getAllMoves(currentState)
        for m in possibleMoves:   
            lastMove = ''
            if(len(path)>0):
                lastMove = path[len(path) - 1]
            potentialScore = currentScore + evaluateDif(currentState,m,goalState)
            if (not(isOpposite(m,lastMove)) and potentialScore<maxDepth):
                cscopy = copy.deepcopy(currentState)
                pathcopy = copy.deepcopy(path)
                makeMove(cscopy,m)
                pathcopy.append(m)    
                solution = as_rec(cscopy,pathcopy, goalState,maxDepth,potentialScore)
                if(solution != None):
                    return solution
    return None
        
def evaluateStartScore(currentState,goalState):
    count = 0
    for i in range(len(currentState[2])):
        for j in range(len(currentState[2][i])):
            if(currentState[2][i][j]!=goalState[2][i][j]):
                count = count + 1
    return count
        
def ASgo(start,goal):
    print("{0} to {1}".format(start,goal))    
    solution = list()
    found = False
    t0 = time.time()
    maxDepth = evaluateStartScore(start,goal)   
    while found == False:
        solution = as_rec(start,list(),goal,maxDepth,evaluateStartScore(start,goal))
        if(solution != None):
            found = True
        else:
            maxDepth = maxDepth + 1
    t1 = time.time()    
    printFinal(t1-t0,solution)