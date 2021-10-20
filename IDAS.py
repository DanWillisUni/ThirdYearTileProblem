# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:17:04 2021

@author: danny
"""

import time
import copy
from State import State
from Helpers import isOpposite,printFinal
    
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
    if(previousState.grid[previousState.blankY + newY][previousState.blankX + newX] == goalState.grid[previousState.blankY][previousState.blankX]):#non zero moves to where it should be
        count = count - 1
    if(goalState.blankX == previousState.blankX + newX and goalState.blankY == previousState.blankY + newY):#zero moves to where it should be
        count = count - 1
    if(previousState.grid[previousState.blankY + newY][previousState.blankX + newX] == goalState.grid[previousState.blankY + newY][previousState.blankX+ newX]):#non zero moves out of where it should be
        count = count + 1
    if(goalState.blankY == previousState.blankY and goalState.blankX == previousState.blankX):#zero moves out of where it should be
        count = count + 1
    return count
        
def as_rec(currentState,path,goalState,maxDepth,currentScore):
    if(currentState.grid==goalState.grid):
        return path;
    else:
        possibleMoves = currentState.getAllMoves()
        for m in possibleMoves:   
            lastMove = ''
            if(len(path)>0):
                lastMove = path[len(path) - 1]
            potentialScore = currentScore + evaluateDif(currentState,m,goalState)
            if (not(isOpposite(m,lastMove)) and potentialScore<maxDepth):
                cscopy = copy.deepcopy(currentState)
                pathcopy = copy.deepcopy(path)
                cscopy.makeMove(m)
                pathcopy.append(m)    
                solution = as_rec(cscopy,pathcopy, goalState,maxDepth,potentialScore)
                if(solution != None):
                    return solution
    return None
        
def evaluateStartScore(currentState,goalState):
    count = 0
    for i in range(len(currentState.grid)):
        for j in range(len(currentState.grid[i])):
            if(currentState.grid[i][j]!=goalState.grid[i][j]):
                count = count + 1
    return count
        
def ASgo(startState,goalState):
    print("{0} to {1}".format(startState,goalState))
    start = State(startState)
    goal = State(goalState) 
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