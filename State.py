# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:05:24 2021

@author: danny
"""

class State:
    def printStateLong(self):
        print("Blank X: ",self.blankX)
        print("Blank Y: ",self.blankY)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if(self.grid[i][j]!=0):
                    print(self.grid[i][j], end=' ')
                else:
                    print(" ",end=' ')
            print()
        #print()
    def printState(self):
        print("[{0}, {1}, {2}]".format(self.blankY,self.blankX,self.grid))
        
    def __init__(self,initList):
        #print("Init",initList);
        self.blankY = initList[0]
        self.blankX = initList[1]
        self.grid = initList[2] 
        if(self.grid[self.blankY][self.blankX]!=0):
            print("Bad starting position")
            self.printState()
        
    def getAllMoves(self):
        allowedMoves = []
        if(self.blankX !=len(self.grid[0]) - 1):
            allowedMoves.append("E")
        if(self.blankX !=0):
            allowedMoves.append("W");
        if(self.blankY !=len(self.grid)-1):
            allowedMoves.append("S")
        if(self.blankY !=0):
            allowedMoves.append("N")
        return allowedMoves
    
    def makeMove(self,direction):
        cont = True
        if(direction == "N"):
            newBlankY = self.blankY - 1
            newBlankX = self.blankX
        elif(direction == "S"):
            newBlankY = self.blankY + 1
            newBlankX = self.blankX
        elif(direction == "E"):
            newBlankY = self.blankY
            newBlankX = self.blankX + 1
        elif(direction == "W"):
            newBlankY = self.blankY
            newBlankX = self.blankX - 1
        else:
            cont = False;
            print("Unrecognised direction",direction)
        if(cont):
            #print("Moving: ",direction)
            self.grid[self.blankY][self.blankX] = self.grid[newBlankY][newBlankX]
            self.grid[newBlankY][newBlankX] = 0
            self.blankY = newBlankY
            self.blankX = newBlankX