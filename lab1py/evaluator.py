import util
import output
import algorithm


def evaluate_optimistic(successor, goal_states, states, heuristic):
    a = 0
    pending_states = list()
    checked_states = dict()

    pending_states[0:0] = states

    while len(pending_states):
        current_starting = pending_states[0]

        *alg_results, final_node = algorithm.search(current_starting, successor, goal_states, heuristic, util.g_ucs,
                                                    util.init_bfs_ucs)

        oracle = 0
        while final_node is not None:
            if final_node[1] not in checked_states:
                if final_node[1] in pending_states:
                    pending_states.remove(final_node[1])
                    # tuple (state, heuristic[state], oracle)
                    checked_states[final_node[1]] = (heuristic[final_node[1]], oracle)
            oracle += final_node[2]  # increase the oracle for the node cost
            final_node = final_node[4]  # move final_node to its parent

    return checked_states


def evaluate_consistent():
    a = 0
