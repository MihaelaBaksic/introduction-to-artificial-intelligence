import loader
import args_parser
import bfs


def main():
    state_space = loader.state_space_loader(args_parser.args.ss)

    if args_parser.args.alg == 'bfs':
        # Initial state, successor, goal_state
        print(bfs.search(state_space[0], state_space[1], state_space[2]))
    elif args_parser.args.alg == 'ucs':
        a = 'call ucs'
    elif args_parser.args.alg == 'astar':
        heuristic = loader.heuristic_loader(args_parser.args.h)
        a = 'call astar'
    else:
        raise ValueError('Wrong alg parameter')


main()
