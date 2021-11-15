# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:12:51 2021

@author: danny
"""

import copy

def getAllMoves(state,lastMove):
    """
    Gets the allowed move directions from the current state

    Ignores a move if it would take it back to the previous state
    EG: if the last move was West it would not return East

    Parameters
    ----------
    state : []
        current state of the problem
    lastMove : str
        Direction that was last moved

    Returns
    -------
    []
        The directions that are possible to move from based on the current state

    """
    allowedMoves = [] #I discovered that a list was more efficient that yielding a next state
    if(state[1] !=len(state[2][0]) - 1 and lastMove != "W"):#if the player can move east and west wasnt the last move
        allowedMoves.append("E")#add east to direction list
    if(state[1] !=0 and lastMove != "E"):#if the player can move west and east wasnt the last move
        allowedMoves.append("W")#add west to direction list
    if(state[0] !=len(state[2])-1 and lastMove != "N"):#if the player can move south and north wasnt the last move
        allowedMoves.append("S")#add south to direction list
    if(state[0] !=0 and lastMove !="S"):#if the player can move north and south wasnt the last move
        allowedMoves.append("N")#add north to direction list
    return allowedMoves#return the list

def makeMove(state,direction):
    """
    Transforms the state by making a move in the direction    

    Parameters
    ----------
    state : []
        current state of the problem
    directione : str
        Direction that needs to be moved

    Returns
    -------
    []
        The state after being transormed by the move in the direction

    """
    newBlankX = state[1]
    newBlankY = state[0]
    if(direction == "N"):#if the direction is north
        newBlankY = state[0] - 1
    elif(direction == "S"):#if the direction is south
        newBlankY = state[0] + 1
    elif(direction == "E"):#if the direction is east        
        newBlankX = state[1] + 1
    elif(direction == "W"):#if the direction is west
        newBlankX = state[1] - 1 
    #make the move on the state
    state[2][state[0]][state[1]] = state[2][newBlankY][newBlankX]
    state[2][newBlankY][newBlankX] = 0
    state[0] = newBlankY
    state[1] = newBlankX

def printFinal(time,solution,moves):  
    """
    Prints the info about each solution to the problem

    Once a solution is found this is called to display how long it took, what the solution was and how many states were looked at

    Parameters
    ----------
    time : double
        time that it took to find the solution
    solution : []
        current state of the problem
    moves : int
        The number of states that were looked at to find the solution to the problem

    """
    print("Time was: {:8.2f} seconds".format(time))#print the time taken
    print("Solution was: ",solution)#print the directions moved
    print("Length: ",str(len(solution)))#print the number of moves taken
    print("Moves: ",moves)#print the number pf moves looked at
    print()
    