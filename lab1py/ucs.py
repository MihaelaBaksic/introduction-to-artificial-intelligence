import path_calc
import heapq


def search(initial_state, successor, goal_state):
    open_nodes = []
    # tuple (g(x), state, cost, accumulated_cost, parent)
    heapq.heappush(open_nodes, (0, initial_state, 0, 0, None))

    # set of traversed states
    closed_states = set()
    closed = 0

    while len(open_nodes) != 0:

        current_node = heapq.heappop(open_nodes)

        if current_node[1] in closed_states:
            continue

        closed_states.add(current_node[1])
        closed += 1

        if current_node[1] in goal_state:
            return 'yes', len(closed_states), current_node[3], path_calc.get_path(current_node[1:])

        for next_state in successor[current_node[1]]:
            if next_state[0] not in closed_states:
                heapq.heappush(open_nodes,
                               ((next_state[1] + current_node[3]),) + next_state
                               + ((next_state[1] + current_node[3]), current_node))

    return 'no', len(closed_states), path_calc.get_path(current_node[1:])
