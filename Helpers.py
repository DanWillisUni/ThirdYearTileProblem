# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:12:51 2021

@author: danny
"""

def isOpposite(move,lastMove):
    if((move == 'N' and lastMove == 'S') or (move == 'W' and lastMove == 'E') or (move == 'E' and lastMove == 'W') or (move == 'S' and lastMove == 'N')):
        return True;
    return False;

def printFinal(total,solution):
    print("Time was: {0} seconds".format(total))
    print("Solution was: ",solution)
    print("Length: ",str(len(solution)))
    print()
    