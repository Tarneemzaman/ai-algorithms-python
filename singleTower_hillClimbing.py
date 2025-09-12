#Single Tower optimization
def heuristic(x, y):
    return 100 - (x - 3) ** 2 - (y - 2) ** 2


def get_neighbours(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbours = []
    for dx, dy in moves:
        temp_neighbour = (x + dx, y + dy)
        if 0 <= temp_neighbour[0] <= 5 and 0 <= temp_neighbour[1] <= 5:  # no grid
            neighbours.append(temp_neighbour)
    return neighbours


def hill_climbing(start_x, start_y):
    current = (start_x, start_y)
    path = [current]

    while True:
        neighbours = get_neighbours(*current)
        if not neighbours:
            break  # no valid neighbours

        # finding base neighbour(max) before comparing
        best_neighbour = neighbours[0]
        for neighbour in neighbours:
            if heuristic(*neighbour) > heuristic(*best_neighbour):  # want closer to goal (utility)
                best_neighbour = neighbour  # now got max in best neighbour

        if heuristic(*best_neighbour) > heuristic(*current):
            current = best_neighbour  # now current is the best one
            path.append(current)
        else:
            break  # stops

    return current, path


initial_positions = [(3, 3), (1, 5), (5, 2)]

for ans in initial_positions:
    final_pos, path = hill_climbing(*ans)
    print(f"Start: {ans}")
    print(f"Path taken: {path}")
    print(f"Final position: {final_pos}")
    print(f"Maximum coverage value: f{final_pos} = {heuristic(*final_pos)}")
    print("-" * 40)
