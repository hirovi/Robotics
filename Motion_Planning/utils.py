'''
Set of useful functions
Author: Oscar Rovira
'''
import time
from math import *

def heuristic_grid(map_grid, goal, method = 'Manhattan', show=False):
    '''
    Function to create heuristic map from given grid.
    It will compute the plain distance values (only takes into account distance cost)
    Constrained to possible directions the robot can go
    Supports Manhattan and Euclidean Distance method.
    '''
    start_time = time.time()
    #Copy map_grid with 0s
    heuristic = [[0 for row in range(len(map_grid[0]))] for col in range(len(map_grid))]

    if method == 'Manhattan':
        #For each node calculate the Manhattan distance
        for r,row in enumerate(heuristic):
            for c,column in enumerate(heuristic[0]):
                dx = goal[0] - c
                dy = goal[1] - r
                heuristic[r][c] = abs(dx) + abs(dy)
        run_time = (time.time() - start_time)

    elif method == 'Euclidean':
        #For each node calculate the Euclidean distance
        for r,row in enumerate(heuristic):
            for c,column in enumerate(heuristic[0]):
                dx = goal[0] - c
                dy = goal[1] - r
                heuristic[r][c] = sqrt(dx * dx + dy * dy)
        run_time = (time.time() - start_time)

    #Show result
    if show:
        for row in heuristic:
            print(row)
        print('Using the {} method'.format(method))
        print('--- {0:.10f} seconds ---'.format(run_time))

    return heuristic_grid


def heuristic_node(x, y, goal, method = 'Manhattan'):
    '''
    Function to calculate the distance from the current node to the goal
    '''
    dx = goal[0] - x
    dy = goal[1] - y

    if method=='Manhattan':
        return abs(dx) + abs(dy)
    elif method=='Euclidean':
        return sqrt(dx*dx + dy*dy)
