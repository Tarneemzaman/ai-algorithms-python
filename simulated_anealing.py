import random
import math


def heuristic(node, goal):
    return abs(node[0]-goal[0])+(node[1]-goal[1])


def get_neighbours(current, grid):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighbours = []
    for move in moves:
        temp_neighbour = (current[0]+move[0], current[1]+move[1])
        if 0 <= temp_neighbour[0] <= 4 and 0 <= temp_neighbour[1] <= 4 and grid[temp_neighbour[0]][temp_neighbour[1]] != 1:
            neighbours.append(temp_neighbour)
    return neighbours


def simulated_annealing(grid, start, goal, T):
    current = start
    path = [current]
    distinct_path = {current}

    while True:
        if T <= 5:
            return False, path
        if current == goal:
            return True, path
        neighbours = get_neighbours(current, grid)
        selected_neighbour = random.choice(neighbours)
        if heuristic(selected_neighbour, goal) <= heuristic(current, goal):
            current = selected_neighbour
            if selected_neighbour not in distinct_path:
                distinct_path.add(selected_neighbour)
                path.append(selected_neighbour)
        else:
            delE = heuristic(selected_neighbour, goal) - \
                heuristic(current, goal)
            prob = math.exp(-delE/T)
            rand_number = random.uniform(0, 1)
            if rand_number <= prob:
                current = selected_neighbour
                if selected_neighbour not in distinct_path:
                    distinct_path.add(selected_neighbour)
                    path.append(selected_neighbour)

        T = T*0.95

        grid = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0]
        ]

    start = (0, 0)
    goal = (4, 4)

    T = 100
    result, path = simulated_annealing(grid, start, goal, T)
    print(result, path)
