# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:12:51 2021

@author: danny
"""
def getAllMoves(state):
    allowedMoves = []
    if(state[1] !=len(state[2][0]) - 1):
        allowedMoves.append("E")
    if(state[1] !=0):
        allowedMoves.append("W");
    if(state[0] !=len(state[2])-1):
        allowedMoves.append("S")
    if(state[0] !=0):
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

def isOpposite(move,lastMove):
    if((move == 'N' and lastMove == 'S') or (move == 'W' and lastMove == 'E') or (move == 'E' and lastMove == 'W') or (move == 'S' and lastMove == 'N')):
        return True;
    return False;

def printFinal(total,solution):
    print("Time was: {0} seconds".format(total))
    print("Solution was: ",solution)
    print("Length: ",str(len(solution)))
    print()
    