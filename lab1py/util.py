
def g_bfs(node, next_state, heuristic):
    return 0


def g_ucs(node, next_state, heuristic):
    return next_state[1] + node[3]


def g_astar(node, next_state, heuristic):
    return heuristic[next_state[0]] + next_state[1] + node[3]


def init_bfs_ucs(state, heuristic):
    return 0


def init_astar(state, heuristic):
    return heuristic[state]
