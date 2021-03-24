
def search(initial_state, successor, goal_state, heuristc):
    open_nodes = list()
    # tuple (state, cost)
    open_nodes.append((initial_state, 0))

    # set of traversed states
    closed_states = set()

    while len(open_nodes) != 0:
        current_node = open_nodes.pop(0)
        closed_states.add(current_node[0])

        if current_node[0] == goal_state:
            return 'yes', len(closed_states)

        for next_node in successor[current_node[0]]:
            if next_node[0] not in closed_states:
                open_nodes.append(next_node)
        # open_nodes sorting
        open_nodes.sort(key=lambda node: (node[1] + heuristc[node[0]]))
        print(open_nodes)

    return 'no', len(closed_states)


def get_path(closed_nodes):
    return 'path', 0  # path and total cost