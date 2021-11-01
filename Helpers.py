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

def isOpposite(move,lastMove):
    if((move == 'N' and lastMove == 'S') or (move == 'W' and lastMove == 'E') or (move == 'E' and lastMove == 'W') or (move == 'S' and lastMove == 'N')):
        return True;
    return False;

def printFinal(time,solution,moves):
    print("Time was: {0} seconds".format(time))
    print("Solution was: ",solution)
    print("Length: ",str(len(solution) - 1))
    print("Moves: ",moves)
    print()
    