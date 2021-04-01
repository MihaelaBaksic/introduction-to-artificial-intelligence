import path_calc
import heapq


def search(initial_state, successor, goal_state, heuristic, g_fun, init_fun):
    open_nodes = []
    init_priority = init_fun(initial_state, heuristic)
    # tuple (g(x), state, cost, accumulated_cost, parent)
    heapq.heappush(open_nodes, (init_priority, initial_state, 0, 0, None))

    # dict of traversed states and their priorities
    closed_states = dict()

    while len(open_nodes) != 0:

        current_node = heapq.heappop(open_nodes)

        if current_node[1] in closed_states and closed_states[current_node[1]] < current_node[0]:
            continue

        closed_states[current_node[1]] = current_node[0]

        if current_node[1] in goal_state:
            return 'yes', len(closed_states), current_node[3], current_node

        for next_state in successor[current_node[1]]:
            priority = g_fun(current_node, next_state, heuristic)
            if next_state[0] not in closed_states or closed_states[next_state[0]] >= priority:
                if next_state[0] in closed_states and closed_states[next_state[0]] >= priority:
                    del closed_states[next_state[0]]
                heapq.heappush(open_nodes,
                               (priority,)
                               + next_state
                               + ((next_state[1] + current_node[3]), current_node))


    return 'no', len(closed_states), current_node
