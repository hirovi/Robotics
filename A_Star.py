'''
A* Implementation
Author: Oscar Rovira
'''

from utils import heuristic
import operator

#Define the map
map = [[0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

#Define where you will start from the map and your goal
start = [0,0]
goal1 = [len(map[0])-1, len(map)-1]
goal2 = [5, 0]
goal = goal2
#Define the possible directions the robot can move
dirs = [[-1, 0 ], # go up
       [ 0, -1], # go left
       [ 1, 0 ], # go down
       [ 0, 1 ]] # go right

dirs_name = ['^', '<', 'v', '>']

#Create heuristic map
heuristic = heuristic(map, goal, method='Manhattan', show=False)
# Output example:
# [6, 5, 4, 3, 2, 3]
# [5, 4, 3, 2, 1, 2]
# [4, 3, 2, 1, 0, 1]
# [5, 4, 3, 2, 1, 2]
# [6, 5, 4, 3, 2, 3]

expansion_grid = [[-1 for row in range(len(map[0]))] for col in range(len(map))]
expansion_grid[goal[1]][goal[0]] = '*'

#Define blocked
#blocked corresponds to the limits of the map and the walls
def is_blocked(map, node):
    if node[0] < 0 or node[0] > (len(map[0])-1) or node[1] < 0 or node[1] > (len(map)-1) or map[node[1]][node[0]] == 1:
        return True
    else:
        return False

optimum_path = []
been_there = []
current_node_pos = start
step = 0
cost = 0
not_finished = True


#A* Algorithm
while(not_finished):
    expansion_grid[current_node_pos[1]][current_node_pos[0]] = step
    been_there.append(current_node_pos)
    possible_dirs_cost = []
    possible_dirs_node = []
    for dir in dirs:
        next_node_pos = [current_node_pos[0] + dir[1], current_node_pos[1] + dir[0]]
        blocked = is_blocked(map, next_node_pos)
        #Check if it's legal to cross
        if blocked == False and next_node_pos not in been_there:
            #Check the cost of this step
            cost = heuristic[next_node_pos[1]][next_node_pos[0]]
            #cost = step + cost
            possible_dirs_cost.append(cost)
            possible_dirs_node.append(next_node_pos)

    min_index, min_value = min(enumerate(possible_dirs_cost), key=operator.itemgetter(1))
    current_node_pos = possible_dirs_node[min_index]
    step +=1

    if current_node_pos == goal:
        not_finished = False
        print('Finished!')
        for row in expansion_grid:
            print(row)
