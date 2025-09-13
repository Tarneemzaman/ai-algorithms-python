#Single Tower optimization
def heuristic(x, y):
    return 100 - (x - 3)**2 - (y - 2)**2


def get_neighbours(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbours = []
    for dx, dy in moves:
        temp_neighbour = (x + dx, y + dy)
        if 0 <= temp_neighbour[0] <= 5 and 0 <= temp_neighbour[1] <= 5:
            neighbours.append(temp_neighbour)
    return neighbours


def hill_climbing(start_x, start_y):
    current = (start_x, start_y)
    path = [current]

    while True:
        neighbours = get_neighbours(current[0], current[1])
        if not neighbours:
            break

        best_neighbour = neighbours[0]
        for neighbour in neighbours:
            if heuristic(neighbour[0], neighbour[1]) > heuristic(best_neighbour[0], best_neighbour[1]):
                best_neighbour = neighbour

        if heuristic(best_neighbour[0], best_neighbour[1]) > heuristic(current[0], current[1]):
            current = best_neighbour
            path.append(current)
        else:
            break

    return current, path


initial_position = [(3, 3), (1, 5), (5, 2)]

for ans in initial_position:
    final_pos, path = hill_climbing(*ans)
    print(f"start:{ans}")
    print(f"path taken :{path}")
    print(f"Final Position:{final_pos}")
    print(f"Maximum coverage value:f{final_pos} = {heuristic(*final_pos)}")

