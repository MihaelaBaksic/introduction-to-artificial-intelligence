import path_calc


def search(initial_state, successor, goal_state):
    open_nodes = list()
    # tuple (g(x), state, cost, accumulated_cost, parent_node)
    open_nodes.append((0, initial_state, 0, 0, None))

    # set of traversed states
    closed_states = set()

    while len(open_nodes) != 0:
        current_node = open_nodes.pop(0)

        if current_node[1] in closed_states:
            continue

        closed_states.add(current_node[1])

        if current_node[1] in goal_state:
            # return found, no_closed_states, total_cost, goal_node
            return 'yes', len(closed_states), current_node[3], current_node

        for next_node in successor[current_node[1]]:
            if next_node[0] not in closed_states:
                open_nodes.append((0,) + next_node + ((next_node[1] + current_node[3]), current_node))

        # print(open_nodes)

    return 'no', len(closed_states), current_node[3], current_node
