# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:12:51 2021

@author: danny
"""

import copy

def getAllMoves(state,lastMove):
    allowedMoves = []
    if(state[1] !=len(state[2][0]) - 1 and lastMove != "W"):
        allowedMoves.append("E")
    if(state[1] !=0 and lastMove != "E"):
        allowedMoves.append("W");
    if(state[0] !=len(state[2])-1 and lastMove != "N"):
        allowedMoves.append("S")
    if(state[0] !=0 and lastMove !="S"):
        allowedMoves.append("N")
    return allowedMoves

def makeMove(state,direction):
    cont = True
    if(direction == "N"):
        newBlankY = state[0] - 1
        newBlankX = state[1]
    elif(direction == "S"):
        newBlankY = state[0] + 1
        newBlankX = state[1]
    elif(direction == "E"):
        newBlankY = state[0]
        newBlankX = state[1] + 1
    elif(direction == "W"):
        newBlankY = state[0]
        newBlankX = state[1] - 1
    else:
        cont = False;
        print("Unrecognised direction",direction)
    if(cont):
        state[2][state[0]][state[1]] = state[2][newBlankY][newBlankX]
        state[2][newBlankY][newBlankX] = 0
        state[0] = newBlankY
        state[1] = newBlankX

def printFinal(time,solution,moves):    
    print("Time was: {:8.2f} seconds".format(time))
    print("Solution was: ",solution)
    print("Length: ",str(len(solution)))
    print("Moves: ",moves)
    print()
    