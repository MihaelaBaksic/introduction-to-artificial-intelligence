import loader
import args_parser
import algorithm
import locale
import output
import evaluator
import util

locale.setlocale(locale.LC_ALL, 'hr_HR')


def main():
    *state_space, states = loader.state_space_loader(args_parser.args.ss)
    heuristic = dict()

    if args_parser.args.alg == 'bfs':
        # Initial state, successor, goal_state
        output.search_output('BFS', args_parser.args.ss,
                             *algorithm.search(*state_space, None, util.g_bfs, util.init_bfs_ucs))
    elif args_parser.args.alg == 'ucs':
        output.search_output('UCS', args_parser.args.ss,
                             *algorithm.search(*state_space, None, util.g_ucs, util.init_bfs_ucs))

    elif args_parser.args.alg == 'astar':
        heuristic = loader.heuristic_loader(args_parser.args.h)
        output.search_output('A-STAR', args_parser.args.ss,
                             *algorithm.search(*state_space, heuristic, util.g_astar, util.init_astar))

    else:
        raise ValueError('Wrong alg parameter')

    if args_parser.args.check_optimistic:
        eval_res = evaluator.evaluate_optimistic(*state_space[1:], states, heuristic)
        output.optimistic_output(eval_res, args_parser.args.h)

    if args_parser.args.check_consistent:
        evaluator.evaluate_consistent()


main()
