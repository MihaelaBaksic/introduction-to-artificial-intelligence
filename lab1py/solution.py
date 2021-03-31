import loader
import args_parser
import bfs
import ucs
import astar
import locale
import output

locale.setlocale(locale.LC_ALL, 'hr_HR')


def main():
    state_space = loader.state_space_loader(args_parser.args.ss)

    if args_parser.args.alg == 'bfs':
        # Initial state, successor, goal_state
        output.search_output('BFS', args_parser.args.ss, *bfs.search(state_space[0], state_space[1], state_space[2]))
    elif args_parser.args.alg == 'ucs':
        output.search_output('UCS', args_parser.args.ss, *ucs.search(state_space[0], state_space[1], state_space[2]))

    elif args_parser.args.alg == 'astar':
        heuristic = loader.heuristic_loader(args_parser.args.h)
        output.search_output('A-STAR', args_parser.args.ss, *astar.search(state_space[0], state_space[1], state_space[2], heuristic))

    else:
        raise ValueError('Wrong alg parameter')


main()
