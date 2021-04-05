import loader
import args_parser
import astar
import locale
import output
import evaluator
import util
import bfs
import ucs
locale.setlocale(locale.LC_ALL, 'hr_HR')


def main():
    # (initial_state, successor, goal_states, all_states)
    *state_space, states = loader.state_space_loader(args_parser.args.ss)
    heuristic = dict()

    if args_parser.args.h:
        heuristic = loader.heuristic_loader(args_parser.args.h)

    if args_parser.args.alg == 'bfs':
        # Initial state, successor, goal_state
        output.search_output('BFS', args_parser.args.ss,
                             *bfs.search(*state_space))
    elif args_parser.args.alg == 'ucs':
        output.search_output('UCS', args_parser.args.ss,
                             *ucs.search(*state_space))

    elif args_parser.args.alg == 'astar':
        output.search_output('A-STAR', args_parser.args.ss,
                             *astar.search(*state_space, heuristic, util.g_astar, util.init_astar))

    if args_parser.args.check_optimistic:
        eval_res = evaluator.evaluate_optimistic(*state_space[1:], states, heuristic)
        output.optimistic_output(eval_res, args_parser.args.h)

    if args_parser.args.check_consistent:
        eval_res = evaluator.evaluate_consistent(state_space[1])
        output.consistent_output(eval_res, args_parser.args.h, heuristic)


main()
