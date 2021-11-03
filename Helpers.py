# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:12:51 2021

@author: danny
"""

import copy

def move(state):    
    if(state[1] !=len(state[2][0]) - 1):
        nextstate = copy.deepcopy(state)
        nextstate[2][state[0]][state[1]] = state[2][state[0]][state[1] + 1]
        nextstate[2][state[0]][state[1] + 1] = 0
        nextstate[1] = state[1] + 1
        yield nextstate
    if(state[1] !=0):
        nextstate = copy.deepcopy(state)
        nextstate[2][state[0]][state[1]] = state[2][state[0]][state[1] - 1]
        nextstate[2][state[0]][state[1] - 1] = 0
        nextstate[1] = state[1] - 1  
        yield nextstate
    if(state[0] !=len(state[2])-1):
        nextstate = copy.deepcopy(state)
        nextstate[2][state[0]][state[1]] = state[2][state[0] + 1][state[1]]
        nextstate[2][state[0] + 1][state[1]] = 0
        nextstate[0] = state[0] + 1
        yield nextstate
    if(state[0] !=0):
        nextstate = copy.deepcopy(state)
        nextstate[2][state[0]][state[1]] = state[2][state[0] - 1][state[1]]
        nextstate[2][state[0] - 1][state[1]] = 0
        nextstate[0] = state[0] - 1
        yield nextstate

def getDirection(firstState,nextState):
    xDif = firstState[1]-nextState[1]
    yDif = firstState[0]-nextState[0]
    if(yDif == -1):
        return "S"
    elif(yDif == 1):
        return "N"
    elif(xDif == -1):
        return "E"
    elif(xDif == 1):
        return "W"

def printFinal(time,solution,moves):
    directions = []
    for x in range(len(solution) - 2):
        directions.append(getDirection(solution[x],solution[x+1]))
    print("Time was: {:8.2f} seconds".format(time))
    print("Solution was: ",directions)
    print("Length: ",str(len(solution) - 1))
    print("Moves: ",moves)
    print()
    