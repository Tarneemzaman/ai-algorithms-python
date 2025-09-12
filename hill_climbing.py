# to get values
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# getting neighbours of a node like 4
def get_neighbours(grid, node):
    neighbours = []
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for move in moves:
        temp_neighbour = (node[0] + move[0], node[1] + move[1])  # node[0] -> row value, move[0] -> colmn value(row,colmn) tuple
        if 0 <= temp_neighbour[0] <= 4 and 0 <= temp_neighbour[1] <= 4 and grid[temp_neighbour[0]][temp_neighbour[1]] != 1:  # row colmn kept in 4 and grid passed
            neighbours.append(temp_neighbour)
    return neighbours  # end (have to find more than once so while loop)

def hill_climbing(grid, start, goal):
    # neighbour detection(1)
    current = start
    path = [start]

    while True:
        if current == goal:  # this condition goal reached
            return True, path

        neighbours = get_neighbours(grid, current)
        if not neighbours:
            break  # no valid neighbours

        # find base neighbour(max) before comparing
        best_neighbour = neighbours[0]
        for neighbour in neighbours:
            if heuristic(neighbour, goal) < heuristic(best_neighbour, goal):  # want closer to goal (lower heuristic)
                best_neighbour = neighbour  # now got min in best neighbour

        if heuristic(best_neighbour, goal) < heuristic(current, goal):
            current = best_neighbour  # now current is the best one
            path.append(current)
        else:
            break  # it stops otherwise (when no neighbouring node present or no best neighbor)

    return False, path

# Grid representation
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0]
]

start = (0, 4) #true
goal = (4, 4)

answer, path = hill_climbing(grid, start, goal)
print(answer, path) #false - > for heuristic path/ value(0,0)
