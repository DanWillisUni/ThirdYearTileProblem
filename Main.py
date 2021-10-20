# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:12:30 2021

@author: danny
"""

from IDDFS import DFSgo as startDFS
from IDAS import ASgo as startAS

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

'''for i in a:
    startDFS(i,goala)
for i in b: 
    startDFS(i,goalb)'''
for i in a:
    startAS(i,goala)
for i in b: 
    startAS(i,goalb)
print("Done")