import loader
import args_parser
import algorithm
import locale
import output

locale.setlocale(locale.LC_ALL, 'hr_HR')


def main():
    state_space = loader.state_space_loader(args_parser.args.ss)

    if args_parser.args.alg == 'bfs':
        # Initial state, successor, goal_state
        output.search_output('BFS', args_parser.args.ss,
                             *algorithm.search(state_space[0], state_space[1], state_space[2], None, g_bfs, init_bfs_ucs))
    elif args_parser.args.alg == 'ucs':
        output.search_output('UCS', args_parser.args.ss,
                             *algorithm.search(state_space[0], state_space[1], state_space[2], None, g_ucs, init_bfs_ucs))

    elif args_parser.args.alg == 'astar':
        heuristic = loader.heuristic_loader(args_parser.args.h)
        output.search_output('A-STAR', args_parser.args.ss,
                             *algorithm.search(state_space[0], state_space[1], state_space[2], heuristic, g_astar, init_astar))

    else:
        raise ValueError('Wrong alg parameter')


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


main()
